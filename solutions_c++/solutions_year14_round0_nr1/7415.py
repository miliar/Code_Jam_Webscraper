#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>
using namespace std;


int main()
{
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    int cases, case_id, arr[2][4][4], row[2];
    for (scanf("%d", &cases), case_id = 1; case_id <= cases; case_id ++)
    {
        for(int i = 0; i < 2; i ++)
        {
            scanf("%d", row + i);
            row[i] --;
            for (int j = 0; j < 4; j ++)
                for (int k = 0; k < 4; k ++)
                    scanf("%d", &arr[i][j][k]);
        }
        int cnt = 0, ans;
        for (int i = 0; i < 4; i ++)
            for (int j = 0; j < 4; j ++)
                if (arr[0][row[0]][i] == arr[1][row[1]][j])
                    ans = arr[0][row[0]][i], cnt ++;
        printf("Case #%d: ", case_id);
        if (cnt == 0)
            puts("Volunteer cheated!");
        else if(cnt == 1)
            printf("%d\n", ans);
        else
            puts("Bad magician!");
    }
}
