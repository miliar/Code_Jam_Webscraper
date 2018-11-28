#include <cstdio>
#include <cstring>
using namespace std;
int flag[11];
void judge(int x)
{
    while(x)
    {
        flag[x%10] = 1;
        x /= 10;
    }
}
int main()
{
    int t,n,i,j,cas = 0;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&t);
    while(t --)
    {
        cas ++;
        scanf("%d",&n);
        if(n == 0)
        {
            printf("Case #%d: INSOMNIA\n",cas);
            continue;
        }
        memset(flag,0,sizeof(flag));
        for(i = 1; i <= 1000; i ++)
        {
            judge(i*n);
            for(j = 0; j < 10; j ++)
            {
                if(flag[j] != 1)
                    break;
            }
            if(j == 10)
            {
                printf("Case #%d: %d\n",cas,i*n);
                break;
            }
        }
    }

}
