#include "stdio.h"
#include "stdlib.h"
#include "string.h"
char c[102];
void re()
{
    int i=strlen(c)-1;
    while(i>-1)
    {
        if(c[i]=='+') c[i]='\0';
        else return;
        i--;
    };
}
main()
{
    freopen("B-Large.in","r",stdin);
    freopen("B-L.txt","w",stdout);
    int t,r,l,i,ans;
    scanf("%d",&t);
    for(r=1;r<=t;r++)
    {
        scanf(" %s",c);
        re();
        l=strlen(c);
        ans=1;
        if(l==0) ans=0;
        for(i=1;i<l;i++)
        {
            if(c[i]!=c[i-1]) ans++;
        }
        printf("Case #%d: %d\n",r,ans);
    }
}
