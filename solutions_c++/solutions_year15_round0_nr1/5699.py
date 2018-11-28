#include<cstdio>
int main()
{
    freopen("input1.txt","r",stdin);
    freopen("output1.txt","w",stdout);
    int t,i,j,s_max,s[1001],k,cnt;
    scanf("%d",&t);
    for(i=0;i<t;i++)
    {
        scanf("%d",&s_max);
        for(j=0;j<=s_max;j++)
            scanf("%1d",&s[j]);
        k=s[0];
        cnt=0;
        for(j=1;j<=s_max;j++)
        {
            if(k>=j) k+=s[j];
            else
            {
                cnt+=(j-k);
                k=j;
                k+=s[j];
            }
        }
        printf("Case #%d: %d\n",i+1,cnt);
    }
    return 0;
}
