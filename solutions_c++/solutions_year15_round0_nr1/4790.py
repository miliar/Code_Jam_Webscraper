#include<stdio.h>
char s[1007];
int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int t,cas=1;
    scanf("%d",&t);
    while(t--)
    {
        int n,count=0;
        scanf("%d",&n);
        scanf("%s",s);
        int i,j;
        int sum=0;
        for(i=0;i<=n;i++)
        {
            int a=s[i]-'0';
            sum+=a;
            if(!(s[i]-'0')&&sum<=i)count++,sum++;
        }
        printf("Case #%d: %d\n",cas++,count);
    }
    return 0;
}
