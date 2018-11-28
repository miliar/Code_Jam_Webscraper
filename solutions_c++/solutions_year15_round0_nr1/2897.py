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
int main()
{
    freopen("input.IN","r",stdin);
    freopen("out.txt","w",stdout);

    int n,i,j,t;
    scanf("%d",&t);
    string s;
    for(int p=1;p<=t;p++)
    {
        cin>>n>>s;
        printf("Case #%d: ",p);
        for(j=0;j<n+1;j++)
        {
            v.push_back(s[j]-'0');
        }
        int prev=0,reqd=0;
        prev+=v[0];
            for(j=1;j<n+1;j++)
            {
                if(j<=prev)
                {
                    prev+=v[j];
                }
                else
                {
                    reqd+=(j-prev);
                    prev=j;
                    prev+=v[j];
                }
            }
            printf("%d\n",reqd);
            v.clear();
    }

     return 0;
}

