#include <stdio.h>
#include <string.h>
#define LL long long 
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define abs(a) ((a)>0?(a):(-1)*(a))

int main()
{
    int i,j,m,n,t;
    char s[205];
    freopen("b.in","r",stdin);
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%s",&s);
        int ans=0;
        for(j=strlen(s)-1;j>=0;j--)
        {
            if(s[j]=='+' && ans%2==1) ans++;
            if(s[j]=='-' && ans%2==0) ans++;
        }
        printf("Case #%d: %d\n",i,ans);
    }
    fclose(stdin);
    return 0;
}
