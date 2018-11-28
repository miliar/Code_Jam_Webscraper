#include<cstdio>
#include<cstdlib>
#include<cstring>

char S[1200];

int main(void)
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int cases;
    scanf("%d",&cases);

    int maxs;
    int ans;
    int i,j;
    for(i=1;i<=cases;i++)
    {

        ans = 0;
        int sum = 0;
        scanf("%d %s",&maxs,S);

        for(j=0;j<=maxs;j++)
        {
            if(sum<j&&S[j]!='0')
            {
                ans+=j-sum;
                sum = j;
            }
            sum+=S[j]-'0';
        }
        printf("Case #%d: %d\n",i,ans);

    }

    return 0;
}
