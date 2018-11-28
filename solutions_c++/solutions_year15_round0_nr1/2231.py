#include<stdio.h>
#include<string.h>
int n,t,cases,ans,sum;
char a;
int main()
{
    while(scanf("%d",&t)!=EOF)
    {
        cases=0;
        while(t--)
        {
            ans=0;
            sum=0;
            cases++;
            scanf("%d",&n);
            scanf("%c",&a);
            for(int i=0;i<=n;i++)
            {
                scanf("%c",&a);
                if((sum<i)&&i!=0)
                {
                    ans++;
                    sum+=1;
                }
                sum+=(a-'0');
            }
            printf("Case #%d: %d\n",cases,ans);
        }
    }
    return 0;
}
