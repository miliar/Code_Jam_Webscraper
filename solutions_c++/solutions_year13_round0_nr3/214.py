
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#define MAX 10000000

using namespace std;

int dig[51];
int sum[102];
vector <string> ps;

void calc(int k, int n) {
    if (2 * k >= n) {
        string num(2 * n - 1, '0');
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                num[i + j] += dig[i] * dig[j];
        // cout << num << endl;
        ps.push_back(num);
        return;
    }

    int start = (k == 0) ? 1 : 0;
    for (int d = start; d <= 3; d++) {
        dig[k] = dig[n - k - 1] = d;
        for (int i = 0; i < 2 * n - 1; i++)
            sum[i] = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                sum[i + j] += dig[i] * dig[j];
        bool overflow = false;
        for (int i = 0; i < 2 * n - 1; i++)
            if (sum[i] > 9) {
                overflow = true;
                break;
            }
        if (!overflow)
            calc(k + 1, n);
    }
    dig[k] = dig[n - k - 1] = 0;
}

void init() {
    for (long long n = 1; n <= 50; n++)
        calc(0, n);
    cerr << "TOTAL: " << ps.size() << endl;
}

inline bool cmp_str(const string &a, const string &b) {
    if (a.size() < b.size())
        return true;
    if (a.size() > b.size())
        return false;
    for (int i = 0; i < a.size(); i++) {
        if (a[i] < b[i])
            return true;
        if (a[i] > b[i])
            return false;
    }
    return true;
}

int solve(const string &A, const string &B) {
    int cnt = 0;
    for (int i = 0; i < ps.size(); i++)
        if (cmp_str(A, ps[i]) && cmp_str(ps[i], B))
            cnt++;
    return cnt;
}

int main() {
    init();

    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        string A, B;
        cin >> A >> B;
        cout << "Case #" << t << ": " << solve(A, B) << endl;
    }
}

