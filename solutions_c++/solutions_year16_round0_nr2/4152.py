#include <iostream>
#include <set>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;
int ans[1000100];

int cal(int x) {
    int flag = 0;
    for (int i = 1; ; i++) {
        int tx = x * i;
        while (tx) {
            flag |= 1 << (tx % 10);
            tx /= 10;
        }
        if (flag == (1 << 10) - 1)
            return i * x;
    }
}

void init() {
    for (int i = 1; i <= 1000000; i++) {
        ans[i] = cal(i);
    }
}

char str[100010];

int main() {
    init();
    freopen("/Users/vino/Desktop/B-large.in", "r", stdin);
    freopen("/Users/vino/Desktop/B-large.out", "w", stdout);
    int T;
    cin >> T;
    int cas = 1;
    while (T--) {
        printf("Case #%d: ", cas++);
        scanf("%s", str);
        int num[110];
        int n = strlen(str);
        for (int i = 0; i < n; i++)
            num[i] = str[i] == '+';
        int flag = 1, tail = n - 1, cnt = 0;
        while (true) {
            int i = tail;
            for (; i >= 0; i--) {
                if (num[i] != flag)
                    break;
            }
            if (i == -1) break;
            cnt++;
            flag ^= 1;
            tail = i;
        }
        cout << cnt << endl;
    }
    return 0;
}