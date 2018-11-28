#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<set>
using namespace std;

void solve()
{
    int row;
    int in = 0;
    int bin[25];
    for(int i=0;i<20;i++)
        bin[i] = 0;
    
    scanf("%d",&row);
    row--;
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            scanf("%d",&in);
            if(i == row)
                bin[in]++;
        }
    }
    
    scanf("%d",&row);
    row--;
    int cnt_2 = 0;
    
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            scanf("%d",&in);
            if(i == row)
                bin[in]++;
            if(bin[in] == 2) cnt_2++;
        }
    }
    if(cnt_2 == 0)
        printf("Volunteer cheated!\n");
    else if(cnt_2 > 1)
        printf("Bad magician!\n");
    else
    {
        for(int i=1;i<=16;i++)
        {
            if(bin[i] == 2)
            {
                printf("%d\n",i);
                
                return ;
            }
        }
    }
}
int main()
{
    int tCase;
    freopen("A-small-attempt1.in","r",stdin);
    freopen("outA.out","w",stdout);
    scanf("%d",&tCase);
    for(int tt=1;tt<=tCase;tt++)
    {
        printf("Case #%d: ",tt);
        solve();
    }
    return 0;
}