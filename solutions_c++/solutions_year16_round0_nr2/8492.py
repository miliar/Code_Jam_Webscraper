#include<stdio.h>
#include<string.h>
char str[108];
int main()
{
   freopen("d:\\codejam\\inb.txt","r",stdin);
   freopen("d:\\codejam\\ob.txt","w",stdout);
   long long i,t,j,l,c;
    scanf("%lld",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%s",str);
        l=strlen(str);
        c=0;
        for(j=l-1;j>-1;j--)
        {
            if(c%2)
            {
                if(str[j]=='+')
                c++;
            }
            else if(str[j]=='-')
            c++;
        }
        printf("Case #%lld: %lld\n",i,c);
    }
    return 0;
}
