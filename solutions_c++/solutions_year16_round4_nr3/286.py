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
#include <cassert>
#include <array>

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


struct vid {
	int i, j, k;
	vid(int i, int j, int k) :i(i), j(j), k(k){}
	vid(){}
};


int R, C;

int vidtoint(vid v){
	return 4 * (C * v.i + v.j) + v.k;
}

vid inttovid(int x){
	vid res;
	res.k = x % 4;
	x /= 4;
	res.i = x / C;
	res.j = x % C;
	return res;
}

void add_edge(VVI &g, vid a, vid b){
	int aint = vidtoint(a), bint = vidtoint(b);
	g[aint].push_back(bint);
	g[bint].push_back(aint);
}

int froml(int l){
	if(l < C)
		return vidtoint(vid(0, l, 0));
	if(l < C + R)
		return vidtoint(vid(l-C, C-1, 1));
	if(l < C + R + C)
		return vidtoint(vid(R-1, C-(l-C-R)-1, 2));
	return vidtoint(vid(R-(l-C-R-C)-1, 0, 3));
}

vector<bool> isev;
void fillisev(){
	for(int l = 0; l < C; l++){
		isev[vidtoint(vid(0, l, 0))] = true;
	}
	for(int l = C; l < C + R; l++){
		isev[vidtoint(vid(l - C, C - 1, 1))] = true;
	}
	for(int l = C + R; l < C + R + C; l++){
		isev[vidtoint(vid(R - 1, C - (l-C-R) - 1, 2))] = true;
	}
	for(int l = C + R + C; l < C + R + C + R; l++){
		isev[vidtoint(vid(R - (l-C-R-C) - 1, 0, 3))] = true;
	}
}

int main(){
	ifstream be("C-small-attempt0.in");
	ofstream ki("ki.txt");
	int T;
	be >> T;
	FOR(tt, T){
		be >> R >> C;
		vector<II> love;
		FOR(i, R + C){
			int x,y;
			be >> x >> y;
			x--; y--;
			love.push_back(MP(x, y));
		}

		isev = vector<bool>(R * C * 4);
		fillisev();

		bool ok;
		int n = R*C;
		int mask;
		for(mask = 0; mask < (1<<n); mask++){
			VVI g(R*C*4);

			int k = 0;
			FOR(i, R){
				FOR(j, C){
					if(!((1 << k)&mask)){
						add_edge(g, vid(i, j, 0), vid(i, j, 3));
						add_edge(g, vid(i, j, 1), vid(i, j, 2));
					} else {
						add_edge(g, vid(i, j, 0), vid(i, j, 1));
						add_edge(g, vid(i, j, 3), vid(i, j, 2));
					}
					k++;

					if(i<R-1)
						add_edge(g, vid(i, j, 2), vid(i + 1, j, 0));
					if(j<C-1)
						add_edge(g, vid(i, j, 1), vid(i, j + 1, 3));
				}
			}

			ok = true;
			FOR(i, R + C){
				int start = froml(love[i].first);
				int end = froml(love[i].second);
				queue<int> q;
				q.push(start);
				vector<bool> vis(R * C * 4);
				vis[start] = true;
				bool end_ok = false;
				bool bad = false;
				while(!q.empty()){
					int u = q.front();
					q.pop();
					FOR(j, SZ(g[u])){
						int v = g[u][j];
						if(!vis[v]){
							vis[v] = true;
							q.push(v);
							if(v == end)
								end_ok = true;
							if(isev[v] && v != end){
								bad = true;
								//break;
							}
						}
					}
				}
				if(!end_ok || bad){
					ok = false;
					break;
				}
			}
			if(ok){
				break;
			}
		}
		if(!ok){
			ki << "Case #" << tt + 1 << ": " << endl << "IMPOSSIBLE" << endl;
		} else {
			ki << "Case #" << tt + 1 << ": " << endl;
			int k = 0;
			FOR(i, R){
				FOR(j, C){
					if(!((1 << k)&mask)){
						ki << '/';
					} else {
						ki << '\\';
					}
					k++;
				}
				ki << endl;
			}
		}
		//ki<<"Case #"<<tt+1<<": "<< <<endl;
		cout << tt << endl;
	}

	ki.close();
	return 0;
}