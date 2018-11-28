#include<iostream>
#include<cstdio>
#include<vector>
#include<map>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<cmath>
#include<algorithm>
#define ll long long
using namespace std;

const ll MOD=1000002013;
const int N = 100001;
struct node
{
    ll o,e;
    ll p;
}a[N];
bool cmp(node x,node y)
{
    if(x.o==y.o)
    return x.e<y.e;
    return x.o<y.o;
}
int main()
{
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    int T;
    cin>>T;
    for(int w=1;w<=T;++w)
    {
        printf("Case #%d: ",w);
        int n;
        ll t;
        cin>>t;
        cin>>n;
        for(int i=0;i<n;++i)
        cin>>a[i].o>>a[i].e>>a[i].p;
        int m=n;
        for(int i=0;i<n;++i)
        {
            while(a[i].p>1)
            {
                a[m].o=a[i].o;
                a[m].e=a[i].e;
                ++m;
                --a[i].p;
            }
        }
        sort(a,a+m,cmp);
        ll sum=0;
        for(int i=0;i<m;++i)
        {
            ll k=a[i].e-a[i].o;
            //cout<<k<<endl;
            sum=(sum+(t+t-k+1)*k/2)%MOD;
        }
        ll ans=0;
        //cout<<m<<endl;
        for(int i=0;i<m;++i)
        {for(int j=i+1;j<m;++j)
        {
            if(a[j].o<=a[i].e&&a[j].e>a[i].e)
            {
                ll tmp=a[i].e;
                a[i].e=a[j].e;
                a[j].e=tmp;
            }

        }
          ll k=a[i].e-a[i].o;
            ans=(ans+(t+t-k+1)*k/2)%MOD;
        }
        //cout<<sum<<" "<<ans<<endl;
        cout<<(sum-ans+MOD)%MOD<<endl;
    }
    return 0;
}
