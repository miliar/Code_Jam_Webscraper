//Caution to the wind,complete freedom
#include<bits/stdc++.h>
#define ll long long
#define MOD 1000000007
ll mpow(ll a, ll n,ll mod)
{ll ret=1;ll b=a;while(n) {if(n&1)
    ret=(ret*b)%mod;b=(b*b)%mod;n>>=1;}
return (ll)ret;
}
using namespace std;
#define pi acos(-1.0)
#define MAXA 1000003
#define sl(n) scanf("%lld",&n)
#define mem(x,a) memset(x,a,sizeof(x))
vector<int> v;
int a[10001];
int main()
{
    freopen("input.IN","r",stdin);
    freopen("out.txt","w",stdout);

    int n,i,j,t;
    scanf("%d",&t);
    for(int p=1;p<=t;p++)
    {
        cin>>n;
        for(j=0;j<n;j++)
            cin>>a[j];
     printf("Case #%d: ",p);
        sort(a,a+n);
        int min1=1e9;
        for(i=1;i<=a[n-1];i++)
        {
            int tm=0,mx=-1;
            for(j=n-1;j>=0;j--)
            {
                if(a[j]>i)
                {
                    int p=a[j]-i,q=a[j]-i;
                    tm++;
                    if(q%i==0)
                    tm+=(q/i-1);
                    else
                        tm+=q/i;

                }

            }
            tm+=i;
            min1=min(min1,tm);
        }
        printf("%d\n",min1);
    }

     return 0;
}

