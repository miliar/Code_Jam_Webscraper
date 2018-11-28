#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define GCD(a,b) __gcd(a, b)
#define mp make_pair
#define DEBUG(x) cout << x << "\n"


int T, N;
string a, b, s1, s2;
int l1[123], l2[123];
int main() {
    ios_base::sync_with_stdio(false);
    cin >> T;
    for (int tc = 1; tc <= T; ++tc) {
        cin >> N;
        cin >> a >> b;
        s1 = "";
        s2 = "";
        s1 += a[0];
        for (int i = 1; i < a.size(); ++i) {
            if (a[i] != a[i - 1])
                s1+= a[i];
        }
        s2 += b[0];
        for (int i = 1; i < b.size(); ++i) {
            if (b[i] != b[i - 1])
                s2 +=  b[i];
        }
        cout << "Case #" << tc << ": ";
        if (s1 != s2) {
            cout << "Fegla Won\n";
            continue;
        }
        for (int i = 0; i <= 100; ++i){
            l1[i] = 0;
            l2[i] = 0;
        }

        int j = 0;
        for (int i = 0; i < s1.size(); ++i) {
            int s = j;
            while (j < a.size() && a[j] == s1[i]) j++;
            l1[i] = j - s;
        }
        j = 0;
        for (int i = 0; i < s2.size(); ++i) {
            int s = j;
            while (j < b.size() && b[j] == s2[i]) j++;
            l2[i] = j - s;
        }
        int ans = 0;
        for (int i = 0; i < s1.size(); ++i) {
            if (l1[i] != l2[i]) {
                ans += abs(l1[i] - l2[i]);
            }
        }
        cout << ans << '\n';
    }
}