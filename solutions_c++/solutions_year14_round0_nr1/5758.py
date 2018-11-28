#include <cstdio>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <string>
#include <climits>
#include <cmath>
#include <queue>
#include <vector>
#include <stack>
#include <set>
#include <map>
#define INF 0x3f3f3f3f
#define eps 1e-8
using namespace std;

int a[4][4], b[4][4];

int main()
{
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int cas;
    scanf("%d", &cas);
    for (int T = 1; T <= cas; T ++)
    {
        int ra, rb;
        scanf("%d", &ra);
        for (int i = 0; i < 4; i ++)
        {
            for (int j = 0; j < 4; j ++)
            {
                scanf("%d", &a[i][j]);
            }
        }
        scanf("%d", &rb);
        for (int i = 0; i < 4; i ++)
        {
            for (int j = 0; j < 4; j ++)
            {
                scanf("%d", &b[i][j]);
            }
        }
        ra --;
        rb --;
        int cot = 0;
        int ans;
        for (int i = 0; i < 4; i ++)
        {
            for (int j = 0; j < 4; j ++)
            {
                if (a[ra][i] == b[rb][j])
                {
                    cot ++;
                    ans = a[ra][i];
                    break;
                }
            }
        }
        printf("Case #%d: ", T);
        if (! cot)
        {
            puts("Volunteer cheated!");
        }
        else if (cot > 1)
        {
            puts("Bad magician!");
        }
        else
        {
            printf("%d\n", ans);
        }
    }
    return 0;
}
