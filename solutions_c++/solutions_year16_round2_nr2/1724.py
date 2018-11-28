#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define ld long double
#define pb push_back
#define mp make_pair
#define pii pair<int, int>
#define pll pair<ll, ll>
#define pdd pair<ld, ld>
#define all(x) (x).begin(), (x).end()
#define fi first
#define se second

int t, n, sol, ansA, ansB;
string a, b, ans;

void back(int k) {
    if (k == n) {
        int A = 0, B = 0;
        for (int i = 0; i < n / 2; i++)
            A = A * 10 + a[i] - '0';
        for (int i = n / 2; i < n; i++)
            B = B * 10 + a[i] - '0';
        if (abs(A - B) < sol) {
            ans = a;
            sol = abs(A - B);
            ansA = A;
            ansB = B;
        } else if (abs(A - B) == sol) {
            if (A < ansA) {
                ans = a;
                sol = abs(A - B);
                ansA = A;
                ansB = B;
            } else if (A == ansA) {
                if (B < ansB) {
                    ans = a;
                    sol = abs(A - B);
                    ansA = A;
                    ansB = B;
                }
            }
        }
        return;
    }

    if (a[k] == '?') {
        for (int i = 0; i < 10; i++) {
            a[k] = i + '0';
            back(k + 1);
            a[k] = '?';
        }
    } else {
        back(k + 1);
    }
}

int main() {
    cin.sync_with_stdio(false);

    cin >> t;
    for (int I = 1; I <= t; I++) {
        cin >> a >> b;
        a += b;
        n = a.size();

        sol = 1 << 30;
        ansA = 1 << 30;
        ansB = 1 << 30;
        back(0);

        ans.insert(ans.begin() + n / 2, ' ');
        cout << "Case #" << I << ": " << ans << '\n';
    }

    return 0;
}
