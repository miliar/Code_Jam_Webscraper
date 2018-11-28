#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
#define de(x) cerr<<#x<<'='<<x<<endl
#define all(x) (x).begin(),(x).end()
#define S(x) scanf("%d",&x)

const int N = 16;
const int J = 50;
int ans = 0;

int isprime(ll n) {
    for (int i = 2; i <= (int)sqrt(n); i++) {
        if (n % i == 0) return i;
    }
    return -1;
}

int helper(int bs, string &s) {
    ll ans = 0;
    ll b = 1;
    for (int i = s.size() - 1; i >= 0; i--) {
        ans += b * (s[i] - '0');
        b *= bs;
    }
    return isprime(ans);
}

vector<int> check(string &s) {
    vector<int> ans;
    for (int i = 2; i <= 10; i++) {
        int tmp = helper(i, s);
        if (tmp == -1) {
            return vector<int>();
        } 
        ans.push_back(tmp);
    }
    return ans;
}

void go(string &s) {
    if (ans == J) return;
    if (s.size() == N - 1) {
        s.push_back('1');
        vector<int> ret = check(s);
        if (ret.size() > 0) {
            ans++;
            cout << s << ' ';
            for (auto ele : ret) cout << ele << ' ';
            cout << endl;
        }
        s.pop_back();
        return;
    }
    s.push_back('0');
    go(s);
    s.pop_back();
    s.push_back('1');
    go(s);
    s.pop_back();
}


int main() {
    puts("Case #1:");
    string s = "1";
    go(s);
}
