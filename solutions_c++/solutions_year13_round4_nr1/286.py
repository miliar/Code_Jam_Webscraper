#include <cstdio>
#include <vector>
#include <queue>
#include <stack>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <set>
#define MAXN 10000
#define MOD 1000002013LL
#define INF
#define PB push_back
#define MP make_pair
#define ST first
#define ND second

#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(a,b,c) for(int a=b;a<=(c);a++)
#define FORD(a,b,c) for (int a=b;a>=(c);a--)
#define VAR(v,n) __typeof(n) v=(n)
#define ALL(c) c.begin(),c.end()
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();i++)

using namespace std;

typedef long long LL;  

int test,n,m,a,b,il,ile;
LL koszt,res;
stack<pair<int,int> > stos;
pair<int,int> t[MAXN];

LL oblicz(int a, int b) {
	int roz = b-a;
	return (((LL(n)*LL(n+1))/2LL)-((LL(n-roz)*LL(n+1-roz))/2LL))%MOD;
}

int main() {
	scanf("%d",&test);
	FOR(g,1,test) {
		scanf("%d%d",&n,&m);
		koszt = res = 0LL;
		ile = 0;
		REP(i,m) {
			scanf("%d%d%d",&a,&b,&il);
			koszt = (koszt+(oblicz(a,b))*LL(il))%MOD;
			t[ile++] = MP(a,-il);
			t[ile++] = MP(b,il);
		}
		//printf("%lld\n",koszt);
		sort(t,t+ile);
		REP(i,ile) {
			if (t[i].ND < 0) stos.push(MP(t[i].ST,-t[i].ND));
				else {
					int pom = t[i].ND;
					while (pom) {
						if (stos.top().ND <= pom) {
							res = (oblicz(stos.top().ST,t[i].ST)*LL(stos.top().ND)+res)%MOD;
							pom -= stos.top().ND;
							stos.pop();
						}
						else {
							res = (oblicz(stos.top().ST,t[i].ST)*LL(pom)+res)%MOD;
							stos.top().ND -= pom;
							pom = 0;
						}
					}
				}
		}
		printf("Case #%d: %lld\n",g,((koszt-res)%MOD+MOD)%MOD);
	}
	return 0;
}
