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

int testy,n,x,res,ilelewo,ileprawo;
bool bylo[100000];
pair<int,int> t[100000];

int main(){
	scanf("%d",&testy);
	FOR(g,1,testy) {
		printf("Case #%d: ",g);
		scanf("%d",&n);
		REP(i,n) {
			scanf("%d",&x);
			t[i] = MP(x,i);
		}
		sort(t,t+n);
		res = 0;
		REP(i,n) bylo[i] = false;
		REP(i,n) {
			//printf("%d %d\n",t[i].ST,t[i].ND);
			bylo[t[i].ND] = true;
			ilelewo = ileprawo = 0;
			FOR(j,0,t[i].ND-1) if (!bylo[j]) ++ilelewo;
			FOR(j,t[i].ND+1,n-1) if (!bylo[j]) ++ileprawo;
			//printf("%d %d\n",ilelewo,ileprawo);
			res += min(ilelewo,ileprawo);
		}
		printf("%d\n",res);
	}
	return 0;
}
