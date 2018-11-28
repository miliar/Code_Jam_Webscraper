#include <bits/stdc++.h>
using namespace std;

#define fi first
#define se second
#define all(x) (x).begin(), (x).end()
typedef long long ll;

const int INF = 0x3c3c3c3c;


char buf[1 << 12];

string exec(string cm) {
    FILE *fp = popen(cm.c_str(), "r");
    fgets(buf, sizeof(buf) - 1, fp);
    string res = string(buf);
    string ans;
    int cnt = 0;
    for (auto c : res) {
        if (cnt && ('0' <= c && c <= '9')) {
            ans.push_back(c);
        }
        if (c == ' ') {
            cnt++;
        }
        if (cnt == 2) {
            break;
        }
    }
    if (cnt < 2) {
        return "";
    }
    return ans;
}

string toStr(__int128 a) {
    stringstream ss;
    if (a / (ll)1e18) {
        ss << (ll)(a / (ll)1e18);
    }
    ss << (ll)(a % (ll)1e18);
    return ss.str();
}

string f(ll x, int b) {
    __int128 p = 1;
    __int128 ans = 0;
    while (x) {
        ans += (x & 1) * p;
        p *= b;
        x /= 2;
    }
    return toStr(ans);
}


int main() {
    #define task "t"
    freopen(task".in", "r", stdin);
    freopen(task".out", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    for (int k = 1; k <= t; k++) {
        int n, j;
        cin >> n >> j;
        cout << "Case #" << k << ":" << endl;
        for (ll i = (1ll << (n - 1)) + 1, cnt = 0; cnt < j; i+= 2) {
            stringstream ss;
            string ans = f(i, 10);
            for (int b = 2; b <= 10; b++) {
                string cur = exec("factor " + f(i, b));
                ans = ans + " " + cur;
                if (cur == "") {
                    ans = "";
                    break;
                }
            }
            if (ans != "") {
                cnt++;
                cout << ans << endl;
            }
        }
    }
    return 0;
}
