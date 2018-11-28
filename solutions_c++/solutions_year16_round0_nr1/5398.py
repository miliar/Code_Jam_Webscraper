/*input

*/

//Template

//Header files
#include <bits/stdc++.h>

//Shortcuts
#define lli long long int
#define fo(i,n) for(i=0;i<n;i++)
#define fi(i,a,n) for(i=a;i<=n;i++)
#define fd(i,n,a) for(i=n;i>=a;i--)
#define modulo 1000000007
#define gi(a) scanf("%d",&a)
#define gs(a) scanf("%d",a)
#define gll(a) scanf("%lld",&a)
#define glf(a) scanf("%lf",&a)
#define gui(a) scanf("%u",&a)
#define f(n) for(i=0;i<n;i++)
#define pn printf("\n")
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define min(a,b) (a<b)?a:b
#define max(a,b) (a>b)?a:b

using namespace std;

int main()
{
	freopen ("A-large.in","r",stdin);
    freopen ("out.txt","w",stdout);
    lli t,tt,n,cnt,mul,dup,digit;
    lli arr[10];
    gll(t);
    for(tt=1;tt<=t;tt++)
    {
        gll(n);
        if(n==0)
        {
            printf("Case #%lld: INSOMNIA\n",tt);
            continue;
        }
        for(lli i=0;i<10;i++)
            arr[i]=0;
        cnt=0;
        mul=1;
        while(true)
        {
            dup=mul*n;
            while(dup>0)
            {
                digit=dup%10;
                if(arr[digit]==0)
                {
                    arr[digit]=1;
                    cnt++;
                }
                dup/=10;
            }
            if(cnt==10)
            {
                printf("Case #%lld: %lld\n",tt,(mul*n));
                break;
            }
            mul++;
        }
    }
    return 0;
}
