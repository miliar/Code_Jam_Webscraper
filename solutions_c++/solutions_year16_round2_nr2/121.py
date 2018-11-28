#include <bits/stdc++.h>

using namespace std;

long long mn;

string s1, s2, ans1, ans2;

long long myabs(long long x) {
    if (x < 0) x = -x;
    return x;
}

long long calc(string x) {
    long long res = 0;
    for (int i = 0; i < x.length(); i++) {
        res = res*10 + x[i] - '0';
    }
    return res;
}

void solve(int test_id) {
    mn = 1E18 + 1E18 + 1E18 + 1E18;
    cin >> s1 >> s2;
    cout << "Case #" << test_id << ": ";
    bool dif = false;
    for (int i = 0; i < s1.length(); i++) {
        if (s1[i] != '?' && s2[i] != '?' && s1[i] != s2[i]) {
            dif = true;
            break;
        }
    }
    if (dif == false) {
        string will1 = s1, will2 = s2;
        for (int i = 0; i < s1.length(); i++) {
            if (will1[i] == '?' && will2[i] == '?') {
                will1[i] = will2[i] = '0';
                continue;
            }
            if (will1[i] == '?') {
                will1[i] = will2[i];
            }
            if (will2[i] == '?') {
                will2[i] = will1[i];
            }
        }
        cout << will1 << " " << will2 << endl;
        return ;
    }
    for (int i = 0; i < s1.length(); i++) {
        bool can = true;
        string t1 = s1, t2 = s2;
        for (int j = 0; j < i; j++) {
            if (t1[j] != '?' && t2[j] != '?' && t1[j] != t2[j]) {
                can = false;
                break;
            }
            if (t1[j] == '?' && t2[j] == '?') {
                t1[j] = t2[j] = '0';
                continue;
            }
            if (t1[j] == '?') {
                t1[j] = t2[j];
            }
            if (t2[j] == '?') {
                t2[j] = t1[j];
            }
        }
        if (can == false) {
            continue;
        }
        for (int d1 = '0'; d1 <= '9'; d1++) {
            for (int d2 = '0'; d2 <= '9'; d2++) {
                if (d1 == d2) {
                    continue;
                }
                string will1 = t1, will2 = t2;
                if (will1[i] == '?') {
                    will1[i] = d1;
                }
                if (will2[i] == '?') {
                    will2[i] = d2;
                }
                if (will1[i] > will2[i]) {
                    for (int j = i + 1; j < s1.length(); j++) {
                        if (will1[j] == '?') {
                            will1[j] = '0';
                        }
                    }
                    for (int j = i + 1; j < s1.length(); j++) {
                        if (will2[j] == '?') {
                            will2[j] = '9';
                        }
                    }
                }
                else {
                    for (int j = i + 1; j < s1.length(); j++) {
                        if (will1[j] == '?') {
                            will1[j] = '9';
                        }
                    }
                    for (int j = i + 1; j < s1.length(); j++) {
                        if (will2[j] == '?') {
                            will2[j] = '0';
                        }
                    }
                }
                long long dif = myabs(calc(will1) - calc(will2) );
                if (dif < mn) {
                    mn = dif;
                    ans1 = will1;
                    ans2 = will2;
                }
                if (dif == mn && will1 < ans1) {
                    mn = dif;
                    ans1 = will1;
                    ans2 = will2;
                }
                if (dif == mn && will1 == ans1 && will2 < ans2) {
                    mn = dif;
                    ans1 = will1;
                    ans2 = will2;
                }
            }

        }
    }
    cout << ans1 << " " << ans2 << endl;
}

int main () {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        solve(i);
    }
    return 0;
}
