#include <cstdio>
#include <vector>
#include <queue>
#include <stack>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <set>
#define MAXN 1000
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

int test,n,wyn_gw,wyn_mo;
int bin[MAXN];
LL p;

int main() {
	scanf("%d",&test);
	FOR(g,1,test) {
		scanf("%d%lld",&n,&p);
		if ((1LL<<(n)) == p) {
			printf("Case #%d: %lld %lld\n",g,p-1LL,p-1LL);
		}
		else if (p == 1) {
			printf("Case #%d: 0 0\n",g);	
		}
		else {
			wyn_gw = wyn_mo = 0;
			--p;
			REP(i,n) bin[i] = (p&1LL), p /= 2LL;
			//REP(i,n) printf("%d ",bin[i]); puts("");
			
			int poz = n-1;
			while (!bin[poz]) --poz; 
			wyn_mo = n-1-poz;
			REP(i,poz) {if (!bin[i]) {++wyn_mo; break;}}
			
			poz = n-1;
			while (bin[poz]) --poz; wyn_gw = n-poz;
			
			printf("Case #%d: %lld %lld\n",g,(1LL<<wyn_gw)-2LL,(1LL<<(n))-(1LL<<wyn_mo));
		}
	}
	return 0;
}
