#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

int T;
int num[4][4];
int key;
int fir[4], sec[4];

void readdata(int key, int a[])
{
    scanf("%d", &key);
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            scanf("%d", &num[i][j]);
            if (i + 1 == key)
            {
                a[j] = num[i][j];
            }
        }
    }
}
int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        readdata(key, fir);
        readdata(key, sec);
        int ret = 0, cnt = 0;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (fir[i] == sec[j]) {
                    cnt++;
                    ret = fir[i];
                }
            }
        }
        if (cnt == 1) {
            printf("Case #%d: %d\n", cas, ret);
        } else if (cnt == 0) {
            printf("Case #%d: Volunteer cheated!\n", cas);
        } else {
            printf("Case #%d: Bad magician!\n", cas);
        }
    }
    return 0;
}
