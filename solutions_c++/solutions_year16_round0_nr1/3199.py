#include<bits/stdc++.h>
#define LL long long int
using namespace std;
int main()
{
   // freopen("A-large.in","r",stdin);
   // freopen("codejam.txt","w",stdout);
    int T,I=1;
    LL all=1023ll;
    scanf("%d",&T);
    while(T--)
    {
    LL n,mask;
    printf("Case #%d: ",I++);
    scanf("%lld",&n);
    if(n==0)
        printf("INSOMNIA\n");
    else
    {
        mask=0;
        LL temp,dig,m=n;
        while(1)
        {
            temp=n;
            while(temp)
            {
            dig=temp%10;
            mask|=(1ll<<dig);
            temp/=10ll;
            }
            if(mask==all)
            {
                printf("%lld\n",n);
                break;
            }
            n+=m;

        }
    }
    }
    return 0;
}
