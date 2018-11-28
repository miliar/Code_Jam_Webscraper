#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
const ll N = 100000;
const ll INF = 1000000000;
const ll md=1000*1000+3;
ll n,t,l,r,m,cas,now;
char a[N];
bool f(ll add)
{
    now=a[0]-'0'+add;
    for (int i=1;i<=n;i++)
        if (now<i)
            return 0;
        else
            now+=a[i]-'0';
    return 1;
}
int main()
{
 //  freopen("sad.in","r",stdin);freopen("out","w",stdout);
    cin>>t;
     cas=0;
    while (t--)
    {
        cas++;
        cin>>n;
        for (int i=0;i<=n;i++)
            cin>>a[i];
         l=0;  r=100000;
        while(l<r)
        {
             m=(l+r)>>1;
            if (f(m)==0)
                l=m+1;
            else
                r=m;
        }
        printf("Case #%lld: %lld\n",cas,r);
    }

}

