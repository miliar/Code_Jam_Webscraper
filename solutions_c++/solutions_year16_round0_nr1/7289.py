#include <bits/stdc++.h>

using namespace std;

typedef pair<int,int> PII;
typedef vector<int> VI;
typedef long long LL;

const int mod = 1000000007;
const int INF = mod;

int main()
{
#ifndef ONLINE_JUDGE
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
#endif
    ios_base::sync_with_stdio(0);
    int T;
    cin >> T;
    for (int cn = 1; cn <= T; cn++) {
        cout << "Case #" << cn << ": ";
        LL N;
        cin >> N;
        set<int> digits;
        bool found = false;
        for (int i = 1; i < 1e5; i++) {
            stringstream ss;
            ss << i * N;
            for (auto& x : ss.str())
                digits.insert(x-'0');
            if (digits.size() == 10) {
                cout << i * N << endl;
                found = true;
                break;
            }
        }
        if (!found) {
            cout << "INSOMNIA\n";
        }
    }
    return 0;
}
