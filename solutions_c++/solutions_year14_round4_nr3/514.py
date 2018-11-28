#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <stack>
#include <math.h>
#include <utility>
#include <iterator>
#include <fstream>
#include <cstdio>
#include <functional>

using namespace std;

template<class T>
string tostring(T a){ stringstream ss; ss << a; return ss.str(); }

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> II;
#define SZ(a) int((a).size()) 
#define PB push_back 
#define ALL(c) (c).begin(),(c).end() 
#define FOR(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
#define LOOP(i,a,b) for((i)=(a);(i)<(b);(i)++)
#define MP(a,b) make_pair((a),(b))
#define LAST(t) (t[SZ(t)-1])




struct szme{
	int c;
	int f;
	szme(int c, int f) :c(c), f(f){}
	szme() :c(-1), f(0){}
};

typedef vector<map<int, szme>> szm_t;

void javit(szm_t &szm, int s, int u, vector<pair<int, bool> > &apa, int &min){
	if(u == s)
		return;
	int v = apa[u].first;
	if(apa[u].second){
		if(min>szm[u][v].f)
			min = szm[u][v].f;
		javit(szm, s, v, apa, min);
		szm[u][v].f -= min;
	} else{
		if(min>szm[v][u].c - szm[v][u].f)
			min = szm[v][u].c - szm[v][u].f;
		javit(szm, s, v, apa, min);
		szm[v][u].f += min;
	}
}

void keresjavut(szm_t &szm, VVI &szl, int s, int t, int &min){
	int n = SZ(szl);
	VI szin(n, 0);
	vector<pair<int, bool> >apa(n); //secondben van, hogy visszamutató-e
	szin[s] = 1;
	queue<int> q;
	q.push(s);
	while(!q.empty()){
		int u = q.front(); q.pop();
		for(int i = 0; i<SZ(szl[u]); i++){
			int &v = szl[u][i];
			if(!szin[v]){
				if(szm[u][v].c != -1 && szm[u][v].f<szm[u][v].c){
					szin[v] = 1;
					apa[v].first = u;
					apa[v].second = false;
					if(v == t){
						javit(szm, s, t, apa, min);
						return;
					}
					q.push(v);
				} else{
					if(szm[v][u].c != -1 && szm[v][u].f>0){
						szin[v] = 1;
						apa[v].first = u;
						apa[v].second = true;
						if(v == t){
							javit(szm, s, t, apa, min);
							return;
						}
						q.push(v);
					}
				}
			}
		}
	}
	min = 0;
}

int ford_fulkerson(szm_t &szm, VVI &szl, int s, int t){
	int fe = 0;
	int min;
	do{
		min = 2000000000;
		keresjavut(szm, szl, s, t, min);
		fe += min;
	} while(min);
	return fe;
}



//returns: folyamertek, folyam (szm)
//cap: matrix (csak ott kell valid ertek, ahol van el)
//(multielekre nem mukodik (tehat ossze kell oket vonni))
//(hurokelnek sem szabad lennie)
int iranyitott_ford_fulkerson(VVI &szl0, vector<map<int,int>> &cap, int s, int t){
	int n = SZ(szl0);
	//vector<vector<szme> > szm(n, vector<szme>(n, szme(-1, 0)));
	szm_t szm(n);
	VVI szl(n);
	FOR(i, n)
		FOR(j, SZ(szl0[i])){
			int u = i, v = szl0[i][j];
			szl[u].push_back(v);
			szl[v].push_back(u);
			szm[u][v].c = cap[u][v]; //emiatt varjuk szomszedsagi matrixkent
			szm[u][v].f = 0;
	}

	int val = ford_fulkerson(szm, szl, s, t);

	//VVI folyam(n, VI(n));
	/*FOR(u, n)
		FOR(v, n)
		folyam[u][v] = szm[u][v].f;*/

	return val;
}





int main(){
	ifstream be("C-small-attempt1.in");
	ofstream ki("ki.txt");
	int T;
	be >> T;
	FOR(tt, T){
		int w, h, b;  be >> w >> h >> b;
		vector<vector<bool> > riv(w, vector<bool>(h));
		FOR(i, b){
			int x0, y0, x1, y1;  be >> x0 >> y0 >> x1 >> y1;
			for(int x = x0; x <= x1; x++){
				for(int y = y0; y <= y1; y++){
					riv[x][y] = true;
				}
			}
		}

		int n = 2*w*h + 2;
		int source = n - 2, sink = n - 1;
		VVI szl(n);
		vector<map<int, int>> cap(n);
		FOR(i, w*h){
			int u = 2 * i, v = 2 * i + 1;
			szl[u].push_back(v);
			cap[u][v] = 1;
		}
		const int xl[]{0, 1, 0, -1};
		const int yl[]{1, 0, -1, 0};
		auto trans = [&](int x, int y){return y*w + x; };
		for(int x = 0; x < w; x++){
			for(int y = 0; y < h; y++){
				if(!riv[x][y]){
					int u = 2 * trans(x, y) + 1;
					for(int k = 0; k < 4; k++){
						int xx = x + xl[k], yy = y + yl[k];
						if(xx >= 0 && xx < w && yy >= 0 && yy < h){
							if(!riv[xx][yy]){
								int v = 2 * trans(xx, yy);
								szl[u].push_back(v);
								cap[u][v] = 1;
							}
						}
					}
				}
			}
		}
		FOR(x, w){
			int v = 2 * trans(x, 0);
			szl[source].push_back(v);
			cap[source][v] = 1;

			int u = 2 * trans(x, h - 1);
			szl[u].push_back(sink);
			cap[u][sink] = 1;
		}

		//auto flow = iranyitatlan_ford_fulkerson(szl, cap, source, sink);
		auto flow = iranyitott_ford_fulkerson(szl, cap, source, sink);
		int sol = flow;


		ki << "Case #" << tt + 1 << ": " << sol << endl;

		cout << tt << endl;
	}


	ki.close();
	return 0;
}