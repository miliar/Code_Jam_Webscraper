#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out2.o","w",stdout);

    int t,n,x,y,i,j,a[10],c;
    scanf("%d",&t);
    for(i=1; i<=t; i++)
    {
        scanf("%d",&n);
        printf("Case #%d: ",i);
        if(n==0)
            printf("INSOMNIA\n");
        else
        {
            for(j=0; j<10; j++)
                a[j]=0;
            j=1,c=0;
            while(1)
            {
                x=j*n;
                while(x>0)
                {
                    y=x%10;
                    x/=10;
                    a[y]++;
                    if(a[y]==1)
                        c++;
                }
                if(c==10)
                {
                    printf("%d\n",j*n);
                    break;
                }
                j++;

            }
        }

    }

    return 0;
}

