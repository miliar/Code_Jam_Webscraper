#include <bits/stdc++.h>

using namespace std;

const int N = 20;
const long long inf = (long long)1e19;

int test;
string a, b;

long long cur_d = inf;

bool check(int num, string s){
    int c[10], i = 0;
    for (int i = 0; i < 10; ++i) c[i] = 0;
    while (num){
        c[s.length() - 1 - i] = num % 10;
        num /= 10;
        ++i;
    }
    for (int i = 0; i < s.length(); ++i){
        if (s[i] == '?') continue;
        if (s[i] != char('0' + c[i])) return false;
    }
    return true;
}

int main()
{
    freopen("B-small-attempt1 (1).in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> test;
    for (int t = 1; t <= test; ++t){
        cin >> a >> b;
        cur_d = inf;
        int len = 1;
        long long ansa, ansb;
        for (int i = 0; i < a.length(); ++i) len *= 10;
        for (int i = 0; i < len; ++i)
        {
            if (!check(i, a)) continue;
            for (int j = 0; j < len; ++j){
                if (!check(j, b)) continue;
                long long d = i - j;
                if (d < 0LL) d = -d;
                if (cur_d > d){
                    ansa = i;
                    ansb = j;
                    cur_d = d;
                } else if (cur_d == d){
                    if (i < ansa){
                        ansa = i;
                        ansb = j;
                    } else if (i == ansa && j < ansb){
                        ansb = j;
                    }
                }
            }

        }
        string A, B;
        while (ansa){
            A += char('0' + ansa%10);
            ansa /= 10;
        }
        while (A.length() != a.length()) A += '0';
        reverse(A.begin(), A.end());

        while (ansb){
            B += char('0' + ansb%10);
            ansb /= 10;
        }
        while (B.length() != a.length()) B += '0';
        reverse(B.begin(), B.end());

        cout << "Case #" << t << ": " << A << " " << B << endl;
    }
    return 0;
}
