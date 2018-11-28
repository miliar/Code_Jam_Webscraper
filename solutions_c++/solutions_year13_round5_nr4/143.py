#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <cstring>
using namespace std;

double ans[1<<20];

int bitcount(int n) {
    int ans = 0;
    while (n > 0) {
        if (n % 2 == 1) {
            ans++;
        }
        n /= 2;
    }
    return ans;
}

bool by_bitcount(int a, int b) {
    return bitcount(a) < bitcount(b);
}

int main() {

    int T;
    cin >> T;

    for (int t = 1; t <= T; t++) {
        string s;
        int n;
        cin >> s;
        n = s.length();
        int index = 0;
        for (int i = n-1; i >= 0; i--) {
            index = 2 * index + (s[i] == 'X');
        }

        vector<int> order(1<<n);
        for (int i = 0; i < (1<<n); i++) {
            order[i] = i;
        }
        sort(order.begin(), order.end(), by_bitcount);

        ans[(1<<n)-1] = 0.0;
        for (int i = (1<<n)-2; i >= index; i--) {
            ans[i] = 0.0;
            for (int pos = 0; pos < n; pos++) {
                int empty = pos;
                int p = n;
                while ((i & (1<<empty)) != 0) {
                    p--;
                    empty++;
                    empty %= n;
                }
                ans[i] += (p + ans[i+(1<<empty)]) / n;
            }
        }

        printf("Case #%d: %.9lf\n", t, ans[index]);
    }

    return 0;
}

