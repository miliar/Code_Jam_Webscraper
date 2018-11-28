#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A_output.txt","w",stdout);
    int T, v1, v2, d;
    bool b1[17],b2[17];
    scanf("%d",&T);
    for (int cases=1;cases<=T;cases++)
    {
        scanf("%d",&v1);
        memset(b1,0,sizeof(b1));
        for (int i=1;i<=4;i++)
        {
            for (int j=1;j<=4;j++)
            {
                scanf("%d",&d);
                if (i==v1) b1[d]=true;
            }
        }
        scanf("%d",&v2);
        memset(b2,0,sizeof(b2));
        for (int i=1;i<=4;i++)
        {
            for (int j=1;j<=4;j++)
            {
                scanf("%d",&d);
                if (i==v2) b2[d]=true;
            }
        }
        int num = 0;
        int result = 0;
        for (int i=1;i<=16;i++)
        {
            if (b1[i] && b2[i])
            {
                num++;
                result = i;
            }
        }
        if (num==0)
        {
            printf("Case #%d: Volunteer cheated!\n",cases);
        }else if (num==1)
        {
            printf("Case #%d: %d\n",cases, result);
        }else{
            printf("Case #%d: Bad magician!\n",cases);
        }
    }
    return 0;
}
