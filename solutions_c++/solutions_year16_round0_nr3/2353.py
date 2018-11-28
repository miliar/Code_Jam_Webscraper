#include <bits/stdc++.h>
#define ll long long
using namespace std;

bool bi[100005];
int dv[100005];

int shit(ll k)
{
    for(int a=2;a<=sqrt(k);a++)
    {
        if(!(k%a)) return a;
    }
    return -1;
}

int main()
{
    freopen("0.in","r",stdin);
    freopen("0.out","w",stdout);


    int a,b,c,d,e,x,y,z,t,n,m;

    scanf("%d",&t);

    for(int te=1;te<=t;te++)
    {
        printf("Case #%d:\n",te);

        scanf("%d %d",&x,&y);

        e=0;

        for(a=(1<<(x-1))+1;a<=(1<<x)-1;a=a+2)
        {
            d=0;
            for(b=2;b<=10;b++)
            {
                ll x=0,y=1;
                for(c=0;c<16;c++)
                {
                    if((a&(1<<c))) x=x+y;
                    y=y*b;
                }
                dv[b]=shit(x);
                if(dv[b]==-1) break;
            }
            if(b>10)
            {
                for(c=15;c>=0;c--)
                {
                    if((a&(1<<c))) printf("1");
                    else printf("0");
                }
                for(b=2;b<=10;b++) printf(" %d",dv[b]); printf("\n");
                e++;
            }
            if(e>=y) break;
        }

    }

    return 0;
}
