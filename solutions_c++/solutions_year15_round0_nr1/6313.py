#include<stdio.h>
int main()
{

    #ifndef CODEJAM
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    #endif

    int ntc,i,j,n,ans,tot;
    char str[1009];
    scanf("%d",&ntc);
    for(j=1;j<=ntc;j++)
    {

    scanf("%d",&n);
    scanf("%s",&str);
    ans=0;
    tot=0;
    for(i=0;i<=n;i++)
    {

        if(str[i]=='0')
            continue;

        else if(tot>=i)
            tot=tot+(str[i]-'0');

        else
        {

            ans=ans+ (i-tot);
            tot=tot+ (i-tot);

        tot=tot+ (str[i]-'0');
        }
    }
        printf("Case #%d: %d\n",j,ans);


    }
}

