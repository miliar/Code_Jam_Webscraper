#include <iostream>
#include <cstdio>
using namespace std;
typedef long long ll;
ll a;
int n;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("Aans.out","w",stdout);
    cin>>n;
    for(int _=1;_<=n;_++)
    {

        cin>>a;
         printf("Case #%d: ",_);
        ll b=a;
        ll beg=0;
        ll des=(1LL<<10)-1;
        if(b==0)
        {
            printf("INSOMNIA\n");
        }
        else
        {
            int ans=0;
            while(beg!=des)
            {
                ll c=b;
                while(c)
                {
                    int d=c%10;
                    beg|=(1LL<<d);
                    c/=10;
                }
                ans++;
                b+=a;
            }
            printf("%lld\n",b-a);
        }
    }
    return 0;
}
