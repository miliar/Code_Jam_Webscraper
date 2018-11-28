#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int t, a[4][4], b[4][4], ca = 1, i, j, one, two, flag = 0,ans = 0;
    scanf("%d",&t);
    while(t--)
    {
        flag = ans = 0;
        scanf("%d",&one);
        for(i = 0;i<4;i++)
            for(j = 0;j<4;j++)
                scanf("%d",&a[i][j]);

        scanf("%d",&two);
        for(i = 0;i<4;i++)
            for(j = 0;j<4;j++)
                scanf("%d",&b[i][j]);

        for(i = 0;i<4;i++)
            for(j = 0;j<4;j++)
                if(a[one-1][i]==b[two-1][j])
                {
                    flag++;
                    ans = a[one-1][i];
                }

        if(flag==0)
            printf("Case #%d: Volunteer cheated!\n", ca++);
        else if(flag==1)
            printf("Case #%d: %d\n", ca++, ans);
        else
            printf("Case #%d: Bad magician!\n", ca++);
    }
}
