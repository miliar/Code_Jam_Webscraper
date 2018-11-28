#include <cstdio>
#include <vector>
#include <queue>
#include <stack>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <set>
#define MAXN
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

int testy,res,ktore,n,x;
int t[100000];
bool bylo[100000];

int main(){
	scanf("%d",&testy);
	FOR(g,1,testy) {
		printf("Case #%d: ",g);
		scanf("%d%d",&n,&x);
		REP(i,n) scanf("%d",&t[i]);
		sort(t,t+n);
		
		res = 0;
		REP(i,n) bylo[i] = false;
		//REP(i,n) printf("%d\n",t[i]);
		FORD(i,n-1,0) if (!bylo[i]) {
			ktore = -1;
			REP(j,n) if (i != j && t[j] + t[i] <= x && !bylo[j])
				ktore = j;
			
			if (ktore != -1) bylo[ktore] = true;
			
			bylo[i] = true;	
			
			//printf("%d %d\n",t[i],t[ktore]);
			++res;	
		}
		printf("%d\n",res);
	}
	return 0;
}
