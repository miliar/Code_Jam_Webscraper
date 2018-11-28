#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

void setNum(long long num, int &flag) {
    if (!num) {
        flag |= 1;
        return;
    }
    while (num) {
        int d = num % 10;
        flag |= 1 << d;
        num /= 10;
    }
}
int main()
{
    int n;
    scanf("%d", &n);
    int finalFlag = 0x3FF;
    for (int i = 1; i <= n; ++i) {
        int num;
        scanf("%d", &num);
        if (num == 0) {
            printf("Case #%d: INSOMNIA\n", i);
            continue;
        }

        int flag = 0;
        int j = 1;
        long long now = 0;
        while (true) {
            now += num;
            setNum(now, flag);
            if (flag == finalFlag) {
                printf("Case #%d: %d\n", i, now);
                break;
            }
        }
    }

    return 0;
}
