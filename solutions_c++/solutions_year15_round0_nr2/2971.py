#include "bits/stdc++.h"
#define puba push_back
#define mapa make_pair
#define ff first
#define ss second
#define bend(_x) (_x).begin(), (_x).end()
#define szof(_x) ((int) (_x).size())

using namespace std;
typedef long long LL;
typedef pair <int, int> pii;

int t;

int main() {    
    //freopen(".in", "r", stdin);
    //freopen(".out", "w", stdout);

    cin >> t;

    for (int i = 0; i < t; ++i) {
        int n;
        cin >> n;
        vector <int> v;
        for (int j = 0; j < n; ++j) {
            int num;
            cin >> num;
            v.puba(num);
        }
        int l = 0, r = 1005;
        while (r - l > 1) {
            int m = (r + l) / 2;
            bool flag = false;

            for (int j = 0; j < m; ++j) {
                int now = m - j;
                int num = 0;
                for (int k = 0; k < n; ++k) {
                    if (v[k] > now) {
                        num += (v[k] - now + now - 1) / now;
                    }
                }
                if (num <= j) {
                    flag = true;
                    break;
                }
            }
            if (flag) {
                r = m;
            } else {
                l = m;
            }
        }
        cout << "Case #" << i + 1 << ": " << r << endl;
    }

    return 0;
}