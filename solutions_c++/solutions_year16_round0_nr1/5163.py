#include<bits/stdc++.h>
using namespace std;
int V[10];

int main()
{


    freopen("A-large.in","r",stdin);
    freopen("out1.txt","w",stdout);
     int t,i;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        long long int n,q,r;
        int ct=0,fg=0;
        scanf("%lld",&n);
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",i);
            continue;
        }


        memset(V,0,sizeof V);
        long long int x=n;
        while(1)
        {   q=x;
            while(q!=0)
            {
                r=q%10;
                if(V[r]==0)
                {
                    V[r]=1;
                    ct++;
                }
                if(ct==10)
                {
                    fg=1;
                    break;
                }
                q=q/10;

            }
            if(fg)
                break;
            x+=n;
        }
        printf("Case #%d: %lld\n",i,x);

    }
    return 0;
}
