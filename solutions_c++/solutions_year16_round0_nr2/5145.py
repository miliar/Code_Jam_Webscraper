#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define pp pair<ll, int>
#define fi first
#define se second
#define esp 1e-12
#define inf 1000000001
#define N 400000
typedef long long ll;
using namespace std;
int nt;
string s;

int main() {
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    cin >> nt;
    for (int kk = 1; kk <= nt; kk++) {
        cin >> s;
        s = s + '+';
        int ret = 0;
        int n = s.size() - 1;
        while (n >= 0 && s[n] == '+') n--;
        if (n >= 0) {
            for (int i = 0; i <= n; i++)
                if (s[i] != s[i + 1]) ret++;
        }
        cout << "Case #" << kk << ": " << ret << "\n";
    }
    /**/return 0;
}
