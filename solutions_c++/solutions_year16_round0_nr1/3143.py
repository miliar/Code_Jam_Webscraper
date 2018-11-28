#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
    ll t,n,p,i,j,r,c=1;
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%lld",&t);
    while(t--)
    {
        scanf("%lld",&n);
        printf("Case #%lld: ",c++);
        if(n==0)
        {
            printf("INSOMNIA\n");
        }
        else
        {
            i=1;
            ll a[15];
            memset(a,0,sizeof(a));
            ll count1=10;
            while(i)
            {


                p=n*i;

                while(p!=0)
                {
                    int r=p%10;
                    //a[r]++;
                    if(a[r]==0)
                    {
                        a[r]=1;
                        count1-=1;
                    }
                    p=p/10;
                }
                if(count1==0)
                break;
                i=i+1;
            }
            ll x=n*i;
            printf("%lld\n",x);

        }
    }
    return 0;
}
