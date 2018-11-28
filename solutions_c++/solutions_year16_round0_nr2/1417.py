
#include <iostream>
#include <string>
#include <queue>
#include <vector>
using namespace std;

int turn(int x, int n) {
    int y = x, i;
    y &= ~((1 << n) - 1);
    for (i = 0; i < n; i++)
        if ((x & (1 << i)) == 0)
            y |= 1 << (n - i - 1);
    return y;
}

int solve(string s) {
    int n = s.size(), i, j, x;
    vector<int> a(1 << n, -1);
    for (x = 0, i = 0; i < n; i++)
        if (s[i] == '+')
            x |= 1 << i;
    a[x] = 0;
    queue<int> q;
    q.push(x);
    int last = (1 << n) - 1;
    while (q.size()) {
        x = q.front();
        q.pop();
        if (x == last)
            break;
        for (j = 1; j <= n; j++) {
            int t = turn(x, j);
            if (a[t] < 0) {
                a[t] = a[x] + 1;
                q.push(t);
            }
        }
    }
    return a[last];
}

string flip(const string &s, int p, int n) {
    char t[101];
    int i;
    for (i = 0; i < p; i++)
        t[i] = (s[p - i - 1] == '-') ? '+' : '-';
    for (; i < n; i++)
        t[i] = s[i];
    return string(t, n);
}

int solve2(const string &s) {
    int n = s.size();
    while (n > 0 && s[n - 1] == '+')
        --n;
    if (!n) return 0;
    int m;
    for (m = 0; m < n; m++)
        if (s[m] != '-') break;
    if (m == n) return 1;
    int p, c, l, i;
    for (p = c = i = 0; i < n; i++) {
        if (s[i] == '+') {
            if (++c > p) p = c, l = i;
        } else
            c = 0;
    }
    int best = m ? solve2(flip(s, n, n)) + 1 : solve2(flip(flip(s, l + 1, n), n, n)) + 2;
    return best;
}

int main() {
    int N, i;
    cin >> N;
    for (i = 0; i < N; i++) {
        string s;
        cin >> s;
        cout << "Case #" << (i + 1) << ": "
             << solve2(s) << endl;
    }
    return 0;
}
