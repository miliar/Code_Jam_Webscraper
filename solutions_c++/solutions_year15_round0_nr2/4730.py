#include<bits/stdc++.h>
#define D 1000000007
#define gcd __gcd
#define getcx getchar
#define pc putchar
#define get(x) scanf("%d",&x)
#define getl(x) scanf("%lld",&x)
#define print(x) printf("%d\n",x)
#define printl(x) printf("%lld\n",x)
#define bitcount __builtin_popcount
using namespace std;
typedef long long ll;
int a[1005];
int main()
{
    int t,j; get(t);
    for(j=1;j<=t;j++)
    {
        int n,x; get(n);
        int i,ans=INT_MAX,sum,mx=0;
        for(i=0;i<n;i++)
        {
            get(a[i]);
            mx=max(mx,a[i]);
        }
        for(x=1;x<=mx;x++)
        {
            sum=0;
            for(i=0;i<n;i++)
            {
                sum+=(a[i]-1)/x;
            }
            sum+=x;
            ans=min(ans,sum);
        }
        cout << "Case #" << j << ": " << ans << endl;
    }
    return 0;
}
