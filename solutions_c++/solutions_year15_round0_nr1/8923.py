#include<cstdio>
int main()
{
    int t,num,si;
    char c[1005];
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        scanf("%d",&si);
        scanf("%s",c);
        int needmore=0,sum=0;
        for(int now=0;now<=si;now++)
        {
            if(c[now]!='0')
            {
                if(sum>=now)
                {
                    sum+=(c[now]-'0');
                }
                else
                {
                    needmore+=(now-sum);
                    sum=now+(c[now]-'0');
                }
            }
        }
        printf("Case #%d: %d\n",i+1,needmore);
    }
    return 0;
}
