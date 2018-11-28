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

int main() {
    init();
    freopen("/Users/vino/Desktop/A-large.in", "r", stdin);
    freopen("/Users/vino/Desktop/A-large.out", "w", stdout);
    int T;
    cin >> T;
    int cas = 1;
    while (T--) {
        printf("Case #%d: ", cas++);
        int n;
        cin >> n;
        if (n == 0) cout << "INSOMNIA" << endl;
        else
            cout << ans[n] << endl;
    }
    return 0;
}