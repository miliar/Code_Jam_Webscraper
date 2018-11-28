#include <bits/stdc++.h>
using namespace std;
#define ll long long
int dig[10];
void check(ll n)
{
    while(n)
    {
        int rem=n%10;
        dig[rem]++;
        n/=10;
    }
}

bool found(ll n)
{
    for(int i=0;i<10;i++)
    {
        if(!dig[i])
            return false;
    }
    return true;
}
int main()
{
    ll t,a;
    FILE *f=freopen("output.txt","w",stdout);
    FILE *in=freopen("input.txt","r",stdin);
    scanf("%lld",&t);
    for(ll tc=1;tc<=t;tc++)
    {
        memset(dig,0,sizeof(dig));
        scanf("%lld",&a);
        ll prev=a;
        for(int i=1;;i++)
        {
            check(a*i);
            //cout<< "ok : "<<a*i<<endl;
            //for(int j=0;j<10;j++)
               // cout<<dig[j]<< " ";
           // cout<<endl;
            if(found(a*i))
            {
                printf("Case #%lld: %lld\n",tc,a*i);
                break;
            }
            else if(prev==a*i && i>1)
            {
                printf("Case #%lld: INSOMNIA\n",tc);
                break;
            }
            else
                prev=a*i;
        }
    }
    fclose(in);
    fclose(f);
    return 0;
}
