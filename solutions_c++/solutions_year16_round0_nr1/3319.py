#include<cstdio>
#include<stdlib.h>

int a[15];
int main()
{
    freopen("abc.txt","w",stdout);
    int t;
    int n;
    int i,j;
    int h;
    int k;
    int x,y;
    scanf("%d",&t);
    for(h=1;h<=t;h++)
    {
        scanf("%d",&n);
        k=0;
        for(i=0;i<=9;i++)
        {
            a[i]=0;
        }
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",h);
        }
        else
        {
            x=n;
            y=1;
            while(k<10)
            {
                while(x)
                {
                    if(a[x%10]==0)
                    {
                        k++;
                        a[x%10]=1;
                    }
                    x/=10;
                }
                y++;
                x=y*n;
            }
            printf("Case #%d: %d\n",h,(y-1)*n);
        }
    }
}
