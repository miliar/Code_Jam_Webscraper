#include <bits/stdc++.h>
using namespace std;

#define S(x) scanf("%d",&x)
#define S2(x,y) scanf("%d%d",&x,&y)
#define S2L(x,y) scanf("%lld%lld",&x,&y)
#define SC(x) scanf("%c",&x)
#define SL(x) scanf("%lld",&x)
#define SS(x) scanf("%s",x)
#define FOR(i, s, e) for(i = s; i < e; i++)
#define FORD(i, e, s) for(i = e; i >= s; i-- )
#define FORSQ(i, s, e) for(i = s; i*i< e; i++)
#define SA(a, s, e) for(i = s; i < e; i++) scanf( "%d" , &a[i])
#define SAL(a, s, e) for(i = s; i < e; i++) scanf("%lld" , &a[i])
#define PA(a, s, e) for(i = s; i < e; i++) printf( "%d" , a[i])
#define P(x) printf("%d",(x))
#define PL(x) printf("%lld",(x))
#define PS(x) printf("%s",(x))

#define SA2D(a, r, c) FOR(i,0,r) FOR(j,0,c) S(a[i][j])

#define ll long long int
#define llu unsigned long long int

#define NL printf("\n")
#define SP printf(" ")
#define pb push_back
#define mp make_pair
#define ppb pop_back
#define pii pair<int,int>
#define pll pair<ll,ll>

#define CLR(a) memset(a,0,sizeof(a))
#define SET(a) memset(a,1,sizeof(a))

#define MOD 1000000007
#define ARRMAX 1000000
#define MAX INT_MAX
#define MIN INT_MIN


int main()
{
	int t,i,j,ans,cnt,n1,n2,a[5][5],b[5][5],tc = 0;
	S(t);
	while(t--){
		cnt = 0;
		tc++;
		S(n1);
		FOR(i,0,4)
			FOR(j,0,4)
				S(a[i][j]);
		S(n2);
		FOR(i,0,4)
			FOR(j,0,4)
				S(b[i][j]);
		FOR(i,0,4){
			FOR(j,0,4){
				if(a[n1-1][i] == b[n2-1][j]){
					ans = a[n1-1][i];
					cnt++;
				}
			}
		}
		printf("Case #%d: ",tc);
		if(cnt == 1){
			printf("%d\n",ans);
		}
		else if(cnt == 0){
			printf("Volunteer cheated!\n");
		}
		else{
			printf("Bad magician!\n");
		}
	}
	return 0;
}