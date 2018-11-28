#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int grid[5][5];
int grid2[5][5];
int main()
{
    freopen("in.txt", "r", stdin);
    int i;
    int T;
    int key;
    int cas = 1;
    int first,second;
    scanf("%d",&T);
    while (T--) {
        scanf("%d",&first);
        first--;
        for (i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                scanf("%d",&grid[i][j]);
        scanf("%d",&second);
        second--;
        for (i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                scanf("%d",&grid2[i][j]);
        int flag = 0;
        int num;
        for (i = 0; i < 4; i++) {
            key = grid[first][i];
            for (int j = 0; j < 4; j++) {
                if (key == grid2[second][j]) {
                    flag++;
                    num = key;
                }
            }
        }
        printf("Case #%d: ",cas++);
        if (flag == 1)printf("%d\n",num);
        if (flag == 0)printf("Volunteer cheated!\n");
        if (flag > 1)printf("Bad magician!\n");
    }
    return 0;
}
