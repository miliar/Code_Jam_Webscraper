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
	int t,tc = 0;
	double c,f,x,ans,temp,rate,curr,prev,total,sum;
	S(t);
	while(t--){
		ans = 0;
		tc++;
		scanf("%lf %lf %lf",&c,&f,&x);
		prev = x/2;
		ans = prev;
		rate = 2;
		sum = 0;
		while(1){
			temp = c/rate;
			rate += f;
			curr = x/rate;
			if(sum + temp + curr >= prev){
				sum += (x/(rate-f));
				break;
			}
			else{
				sum += temp;
				prev = sum + curr;
			}
		}
		printf("Case #%d: ",tc);
		printf("%.7lf\n",min(ans,sum));
	}
	return 0;
}