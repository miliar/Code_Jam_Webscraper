#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

#define pb push_back
#define mp make_pair

#define ALL(x) (x).begin(),(x).end()
#define CLR(a,b) memset(a,b,sizeof(a))
#define REPN(x,a,b) for (int x=a; x<b;++x)
#define REP(x,b) REPN(x, 0, b)

#define dbg(x) cout << #x << " = " << x << endl;
#define dbg2(x, y) cout << #x << " = " << x << "  " << #y << " = " << y << endl;
#define dbg3(x, y, z) cout << #x << " = " << x << "  " << #y << " = " << y << "  " << #z << " = " << z << endl;
#define dbg4(x, y, z, w) cout << #x << " = " << x << "  " << #y << " = " << y << "  " << #z << " = " << z << "  " << #w << " = " << w <<  endl;
#define INF 1<<20

vector<vector<pair<char, int> > > V;

int main() {
	int t,cas,n,ax;
	string cad;
	scanf("%d",&t);
	for (cas = 1; cas <= t; ++cas) {
		V.clear();
		scanf("%d",&n);
		REP(i,n){
			cin>>cad;
			ax = 0;
			vector<pair<char, int> > P;
			int j=0;
			while(j<cad.length()){
				ax = 1; char aux = cad[j];
				while(j<cad.length() && cad[j]==aux){
					ax++; j++;
				}
				P.pb(mp(aux,ax));
			}
			V.pb(P);
		}

		int mini = INF, acum;
		REPN(i,1,100){
			vector<pair<char,int> > P;
			REP(j,V[0].size()){
				P.push_back(make_pair(V[0][j].first,i));
			}
			V.pb(P);
		}
		REP(i,V.size()){
			acum = 0;
			REP(j,n){
				if(j!=i){
					if(V[i].size() != V[j].size()){
						acum=INF; break;
					}
					ax = 0;
					REP(k,V[i].size()){
						if(V[i][k].first==V[j][k].first)
							ax += abs(V[i][k].second-V[j][k].second);
						else{ ax = INF; break; }
					}
					if(ax==INF){ acum = INF; break; }
					else acum += ax;
				}
			}
			mini = min(mini,acum);
		}
		if(mini==INF) printf("Case #%d: Fegla Won\n", cas);
		else printf("Case #%d: %d\n", cas, mini);
	}
	return 0;
}