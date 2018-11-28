#include<stdio.h>
int main()
{
    int t,i,n,j,out,standing;
    char s[1002];
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        out=0;
        scanf("%d",&n);
        scanf("%s",s);
        standing=s[0] - '0';
        for(j=1;j<=n;j++)
        {
            if(s[j]>'0')
            {
                if(standing>=j)
                {
                    standing+=s[j]-'0';
                }
                else
                {
                    out+=j-standing;
                    standing=j+(s[j]-'0');
                }
            }
        }
        printf("Case #%d: %d\n",i,out);
    }
    return 0;
}
