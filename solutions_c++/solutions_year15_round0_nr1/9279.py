#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

typedef long long ll;

ll n;

int main() {
    freopen("A-large.txt", "r", stdin);
    freopen("A-small-attempt2.txt", "w", stdout);
    cin >> n;
    for(int i = 0; i < n; i++) {
        ll max_, ans1 = 0, ans = 0;
        string s;
        cin >> max_ >> s;
        //cout << "HI" << endl;
        for(int j = 0; j < s.size(); j++) {
            if (s[j] != '0' && ans1 >= j) {
                ll a = s[j] - '0';
                ans1+=a;
                continue;
            }
            if (s[j] != '0' && ans1 < j) {
                ll a = s[j] - '0';
                ans+=(j-ans1);
                ans1+=(j-ans1);
                ans1+=a;
                continue;
            }
        }
        cout << "Case #" << i + 1 << ": " << ans << endl;
    }
    return 0;
}
