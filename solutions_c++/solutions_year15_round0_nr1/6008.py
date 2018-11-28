#include<stdio.h>
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,n,aud,ct,i,j;
    char s[1005];
    scanf("%d",&t);
    for(i=0;i<t;i++)
    {
        aud=0;
        ct=0;
        scanf("%d%s",&n,s);
        for(j=0;j<=n;j++)
        {
            if(aud<j)
            {
                ct+=(j-aud);
                aud=j;
            }
            aud+=(int)(s[j]-48);
        }
        printf("Case #%d: %d\n",i+1,ct);
    }
}
