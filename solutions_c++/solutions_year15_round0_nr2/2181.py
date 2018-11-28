#include<cstdio>
#include<cstdlib>
#include<cstring>

int P[1050];


int main(void)
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int cases;
    scanf("%d",&cases);
    int D;

    int i,j,k;
    for(i=1;i<=cases;i++)
    {
        int ans = 0;
        int maxs = 0;
        scanf("%d",&D);
        for(j=0;j<D;j++)
        {
            scanf("%d",&P[j]);
            if(P[j]>ans)
                ans = P[j];
        }
        maxs = ans;
        int tmp = 0;
        for(j=1;j<=maxs;j++)
        {
            tmp = 0;
            for(k=0;k<D;k++)
            if(P[k]>j)
            {
                tmp+=(P[k]/j);
                if(P[k]%j==0)
                    tmp--;
            }
            tmp+=j;
            if(tmp<ans)
                ans = tmp;
        }
        printf("Case #%d: %d\n",i,ans);
    }

    return 0;
}
