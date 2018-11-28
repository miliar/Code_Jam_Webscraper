#include <cstdio>
#include <cstring>
#include <queue>
using namespace std;
#define LL __int64
LL pow[11][21];
bool isPrim(LL num)
{
    for(LL i = 2; i*i <= num; i ++)
    {
        if(num%i == 0)
            return false;
    }
    return true;
}
void fuck(LL num)
{
    for(LL i = 2; i*i <= num; i ++)
    {
        if(num%i == 0)
        {
            printf(" %I64d",i);
            return;
        }
    }
}
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int t,cas=0;
    int N,J,i,j,k;
    scanf("%d",&t);
    for(int i = 2; i <= 10; i ++)
    {
        pow[i][0] = 1;
        for(int j = 1; j <= 16; j ++)
            pow[i][j] = pow[i][j-1]*i;
    }
    while(t--)
    {
        cas ++;
        scanf("%d%d",&N,&J);
        int ans = 0;
        printf("Case #%d:\n",cas);
        for(i = 0; i <(1<<N); i ++)
        {
            if((i&1)&&(i&(1<<(N-1))))
            ;
            else
            continue;
            for(j = 2; j <= 10; j ++)
            {
                LL num = 0;
                for(k = 0; k < N; k ++)
                {
                    if(i&(1<<k))
                        num += pow[j][k];
                }
                if(isPrim(num)) break;
            }
            if(j == 11)
            {
                ans ++;
                for(j = N-1; j >= 0; j --)
                {
                    if(i&(1<<j))
                        printf("1");
                    else
                        printf("0");
                }
                //printf("%d\n",i);
                for(j = 2; j <= 10; j ++)
                {
                    LL num = 0;
                    for(k = 0; k < N; k ++)
                    {
                        if(i&(1<<k))
                            num += pow[j][k];
                    }
                    fuck(num);
                }
                printf("\n");
            }
            if(ans == J) break;
        }
    }
}
