#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define GCD(a,b) __gcd(a, b)
#define mp make_pair
#define DEBUG(x) cout << x << "\n"


int T, A, B, K;
int main() {
    ios_base::sync_with_stdio(false);
    cin >> T;
    for (int tc = 1; tc <= T; ++tc) {
        cin >> A >> B >> K;
        int ans = 0;
        for (int a = 0; a < A; ++a) {
            for (int b = 0; b < B; ++b) {
                int third = (a & b);
                if (third < K){
                    ans++;
                }
            }
        }
        cout << "Case #" << tc << ": " << ans << '\n';
    }
}