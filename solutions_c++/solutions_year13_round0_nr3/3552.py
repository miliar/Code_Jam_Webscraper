#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;

const int MAX = 1002;
int sum[MAX];
int flag[MAX];
int p_cnt;
int n, m;

bool check_p(int x)
{
    int cnt = 0;
    int px = x;
    int *arr = new int[10];
    while (px > 0) {
        arr[cnt++] = px % 10;
        px /= 10;
    }
    for (int i = 0; i < cnt / 2; ++i)
        if (arr[i] != arr[cnt - 1 - i])
            return false;
    return true;


}

void pre()
{
    int p_cnt = 0;
    memset(flag, 0, sizeof(flag));
    for (int i = 1; i * i <= 1000; ++i) {
        if (check_p(i) && check_p(i * i)) {
            flag[i * i] = 1;
          //  printf("hh %d\n", i * i);
        }
    }
    memset(sum, 0, sizeof(sum));
    for (int i = 1; i <= 1000; ++i)
        if (flag[i] == 1)
            sum[i] = sum[i -1] + 1;
        else
            sum[i] = sum[i -1];
}

int main()
{
    freopen("c.in", "r", stdin);
   freopen("c.out", "w", stdout);

    int cas;
    int a, b;
    pre();
    scanf("%d", &cas);
    for (int icase = 1; icase <= cas; ++icase) {
        scanf("%d%d", &a, &b);
        printf("Case #%d: %d\n", icase, sum[b] - sum[a - 1]);
    }

}
