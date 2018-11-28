#include<bits/stdc++.h>
using namespace std;
#define llu unsigned long long int

llu solve(int n)
{
    bool digit[10];
    memset(digit,0,sizeof(digit));
    int i,j,d;
    llu ret,u,x;
    u=n;
    for(i=1;; i++)
    {
        ret=u*i;
        x=ret;
        while(x)
        {
            d=x%10;
            x/=10;
            digit[d]=1;
        }
        for(j=0; j<10; j++) if(!digit[j]) break;
        if(j==10) return ret;
    }
}

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T,n,cs;
    scanf("%d",&T);
    for(cs=1; cs<=T; cs++)
    {
        scanf("%d",&n);
        printf("Case #%d: ",cs);
        if(n) printf("%llu\n",solve(n));
        else printf("INSOMNIA\n");
    }
    return 0;
}
