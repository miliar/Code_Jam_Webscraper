#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    int test, i, j, ans1, ans2, grid[4][4], cs, res, cnt;
    bool flag[17];

    //freopen("A-small-attempt0.in", "r", stdin);
    //freopen("A-small-attempt0.out", "w", stdout);
    cs = 1;
    cin>>test;
    while(test--)
    {
        cnt = 0;
        res = 0;
        for(i=0;i<17;i++)
        {
            flag[i] = false;
        }

        cin>>ans1;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>grid[i][j];
                if(i+1 == ans1)
                {
                    flag[grid[i][j]] = true;
                    //printf("flag[%d] = true\n", grid[i][j]);
                }
            }
        }

        cin>>ans2;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>grid[i][j];
                if(i+1 == ans2 && flag[grid[i][j]])
                {
                    cnt++;
                    res = grid[i][j];
                }
            }
        }
        if(!cnt)
        {
            printf("Case #%d: Volunteer cheated!\n", cs++);
        }
        else if(cnt == 1)
        {
            printf("Case #%d: %d\n", cs++, res);
        }
        else
        {
            printf("Case #%d: Bad magician!\n", cs++);
        }
    }
    return 0;
}
