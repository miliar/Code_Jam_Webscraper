#include <bits/stdc++.h>

using namespace std;


const int N = (int)1e5 + 4;
const int inf = (int)1e9 + 7;


void solve(int t) {
    vector<string> a(10);
    vector<int> cnt(10, 0);
    vector<int> c(26, 0);
    vector<int> d(10, 0);
    string s;
    cin >> s;
    string p = "ZWXUGRSOFI";
    a[0] = "ZERO";
    a[1] = "TWO";
    a[2] = "SIX";
    a[3] = "FOUR";
    a[4] = "EIGHT";
    a[5] = "THREE";
    a[6] = "SEVEN";
    a[7] = "ONE";
    a[8] = "FIVE";
    a[9] = "NINE";
    d[0] = 0;
    d[1] = 2;
    d[2] = 6;
    d[3] = 4;
    d[4] = 8;
    d[5] = 3;
    d[6] = 7;
    d[7] = 1;
    d[8] = 5;
    d[9] = 9;
    for (int i = 0; i < (int)s.size(); ++i) {
        c[s[i] - 'A']++;
    }
    for (int i = 0; i < 10; ++i) {
        int f = c[p[i] - 'A'];
        for (int j = 0; j < (int)a[i].size(); ++j) {
            c[a[i][j] - 'A'] -= f;
        }
        cnt[d[i]] = f;
    }
    cout << "Case #" << t << ": ";
    for (int i = 0; i < 10; ++i) {
        for (int j = 0; j < cnt[i]; ++j) {
            cout << i;
        }
    }
    cout << endl;
    //printf("Case #%d: %d\n", t, answer);
}


int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    //printf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        solve(t);
    }	
    return 0;
}