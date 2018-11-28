#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<vector>
#include<map>
#include<queue>
#include<set>
using namespace std;
typedef long long LL;
#define For(i,a,n) for((i)=(a);(i)<=(n);(i)+=1)
#define refresh(a) memset((a),0,sizeof(a))
#define IN_S(x) scanf("%s",(x))
#define P_S(x) printf("%s\n",x)
#define IN_D(x) scanf("%lf",&(x))
#define P_D(x) printf("%d\n",x)
#define IN_F(x) scanf("%lf",&(x))
#define P_F(x) printf("%lf\n",x)
#define IN_L(x) scanf("%lld",&(x))
#define P_L(x) printf("%lld\n",x)
#define P_NL printf("\n")
#define read() freopen("A-small-attempt0.in","r",stdin)
#define write() freopen("a-small-output.out","w",stdout)
#define INF 1000000
#define mod 1000000007
#define maxn 1000
int arr[maxn];

int main()
{
    read();write();
	double cases,r,t,i,d,ans;
	IN_D(cases);
	For(i,1,cases)
	{
	    IN_D(r),IN_D(t);

	    d=(2*r-1)*(2*r-1)+(8*t);
	    d=sqrt(d);

	    ans=d-(2*r-1);
	    ans/=4;//cout<<d<<" "<<ans<<endl;
	    printf("Case #%d: %lld\n",(int)i,(LL)ans);
	}
	return 0;
}
