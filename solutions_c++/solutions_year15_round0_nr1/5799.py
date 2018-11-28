#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
    int i,j,k,l,m,t,tc,n;
    char s[1002];
    int b[1002];
    scanf("%d",&tc);
    for(t=1;t<=tc;t++)
    {
        scanf("%d",&n);
        scanf("%s",&s);
        for(i=0;i<=n;i++)
        {
            b[i]=s[i]-48;
        }
        l=0;
        k=0;
        for(i=0;i<=n;i++)
        {
            if((i<=l)&&(b[i]>0))
            {
                l=l+b[i];
            }
            else
            {
                if(b[i]>0)
                {
                    m=i-l;
                    k=k+m;
                    l=l+b[i]+m;
                }
            }
        }
        printf("Case #%d: %d\n",t,k);
    }
    return 0;
}
