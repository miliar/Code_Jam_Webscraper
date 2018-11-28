#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
private:
    int n;
    string s;
    int res;
public:
    void input() {
        cin >> n >> s;
    }
    int work(int n, string s) {
        res = 0;
        int cnt = 0;
        for (int i = 0; i <= n; i++) {
            int x = s[i] - '0';
            if (x == 0) continue;
            if (i > cnt) {
                res += (i - cnt);
                cnt += (i - cnt);
            }
            cnt += x;
        }
        return res;
    }
    void output(int kase) {
        printf("Case #%d: %d\n", kase, work(n, s));
    }
};

Solution solver;

int main() {
    int cs; scanf("%d", &cs);
    for (int kase = 1; kase <= cs; kase++) {
        solver.input();
        solver.output(kase);
    }
    return 0;
}
