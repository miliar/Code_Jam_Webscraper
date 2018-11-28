#include<stdio.h>
#include<string.h>
char s[105];
int cake[105];
int main()
{
    int t;
    scanf("%d",&t);
    int cases=0;
    while(t--)
    {
        cases++;
        int ans=0;
        scanf("%s",s);
        printf("%s\n",s);
        int len=strlen(s);
        memset(cake,0,sizeof(cake));
        for(int i=0;i<len;i++)
        {
            if(s[i]=='-')
            {
                cake[i]=0;
            }
            else
            {
                cake[i]=1;
            }
        }
        for(int i=len-1;i>=0;i--)
        {
            if(cake[i]==0)
            {
                for(int j=i;j>=0;j--)
                {
                    cake[j]^=1;
                }
                ans++;
            }
        }
        printf("Case #%d: %d\n",cases,ans);
    }
    return 0;
}
