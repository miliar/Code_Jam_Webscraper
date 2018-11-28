#include <cstdio>
using namespace std;
#define N 4

int a[N][N], b1[N], b2[N], ans[N], sum;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int x = 1; x <= T; x++)
    {
        int num;
        scanf("%d", &num);
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                scanf("%d", &a[i][j]);
        for (int i = 0; i < N; i++)
            b1[i] = a[num - 1][i];
        scanf("%d", &num);
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                scanf("%d", &a[i][j]);
        for (int i = 0; i < N; i++)
            b2[i] = a[num - 1][i];
        sum = 0;
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                if (b1[i] == b2[j])
                {
                    ans[sum++] = b1[i];
                    break;
                }
        printf("Case #%d: ", x);
        switch (sum)
        {
            case 0:
                puts("Volunteer cheated!");
                break;
            case 1:
                printf("%d\n", ans[0]);
                break;
            default:
                puts("Bad magician!");
        }
    }
    return 0;
}
