#include<bits/stdc++.h>
#define X first
#define Y second
#define MEM(x,y) memset(x,y,sizeof x)
using namespace std;
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,cas,a[15],sum;
    long long n,cur,y;
    cin>>t;
    for(cas=1;cas<=t;cas++)
    {
        cin>>n;
        printf("Case #%d: ",cas);
        if(n==0)printf("INSOMNIA\n");
        else
        {
            sum=0,cur=0;
            MEM(a,0);
            while(sum<10)
            {
                cur+=n;
                y=cur;
                while(y)
                {
                    if(!a[y%10])a[y%10]++,sum++;
                    y/=10;
                }
            }
            printf("%lld\n",cur);
        }
    }
}
