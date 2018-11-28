#include<stdio.h>
#include<cstring>
#include<cstdlib>
#include<cmath>
typedef long long int ll;
ll a[4][4];
ll b[4][4];
int main()
{
    int test_cases;
    int ans_1,ans_2;
    scanf("%d",&test_cases);
    for(int i=0;i<test_cases;i++)
    {
        scanf("%d",&ans_1);
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                scanf("%lld",&a[j][k]);
            }
        }
        scanf("%d",&ans_2);
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                scanf("%lld",&b[j][k]);
            }
        }
        int match_count=0;
        ll match_number;
        /* Make sure the numbers of the matrix are distinct. */
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                if(a[ans_1-1][j]==b[ans_2-1][k])
                {
                    match_count++;
                    match_number=a[ans_1-1][j];
                }
            }
        }
        if(match_count>0)
        {
            if(match_count==1)
            {
                printf("Case #%d: %lld\n",i+1,match_number);
            }
            else
            {
                printf("Case #%d: Bad magician!\n",i+1);
            }
        }
        else
        {
            printf("Case #%d: Volunteer cheated!\n",i+1);
        }
    }
}
