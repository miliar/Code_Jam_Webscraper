#include <fstream>
#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>

using namespace std;

int ans[17];
int bd[4][4];

int main()
{
    int T;
    int a, b, x;

    scanf("%d", &T);

    for (int t = 1; t <= T; t++)
    {
        for(int i = 0; i < 17; i++)
            ans[i] = 0;
        scanf("%d", &a);
        a--;
        for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            scanf("%d", &bd[i][j]);
        
        for (int j = 0; j < 4; j++)
            ans[bd[a][j]]++;

        scanf("%d", &b);
        b--;

        for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            scanf("%d", &bd[i][j]);

        for (int j = 0; j < 4; j++)
            ans[bd[b][j]]++;

        int cnt = 0, ret = -1;
        for (int i = 1; i <= 16; i++)
            if (ans[i] == 2)
            {
                cnt++;
                ret = i;
            }

        printf("Case #%d: ", t);
        if (cnt == 1) printf("%d\n", ret);
        else if (cnt > 1) printf("%s\n", "Bad magician!");
        else if (cnt < 1) printf("%s\n", "Volunteer cheated!");
    }

    return 0;
}
