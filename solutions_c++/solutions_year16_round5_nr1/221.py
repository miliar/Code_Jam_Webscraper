#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

#ifndef ONLINE_JUDGE
#define dbg(x) cerr << __LINE__ << " : " << #x << " = " << (x) << endl;
#else
#define dbg(x)
#endif

#define ff first
#define ss second

string str;
void solve(){
    cin >> str;
    int n = (int) str.size();
    stack<char> stk;
    int res = 0;
    for (int i = 0; i < n; i++){
        if (stk.empty()) stk.push(str[i]);
        else if (stk.top() == str[i]) stk.pop();
        else if ((int) stk.size() == (n - i)) {
            res++;
            stk.pop();
        } else stk.push(str[i]);
    }
    int sum = (res * 5) + ((n/2 - res) * 10);
    cout << sum << endl;
}

const int MAXN = 55;
int memo[MAXN][MAXN];
int dp(int L, int R){
    if (L >= R) return 0;
    int &res = memo[L][R];
    if (res != -1) return res;
    res = INT_MAX;
    for (int i = L + 1; i <= R; i += 2){
        int cur = (str[L] != str[i]);
        cur += dp(L + 1, i - 1) + dp(i + 1, R);
        res = min(res, cur);
    }
    return res;
}
int cs;
void solve_slow(){
    memset(memo, -1, sizeof memo);
    cin >> str;
    int n = (int) str.size();
    int res = dp(0, n-1);
    int sum = (res * 5) + ((n/2 - res) * 10);
    cout << sum << endl;
}

int main(){
    std::ios_base::sync_with_stdio(false);
    int tc; cin >> tc;
    for (cs = 1; cs <= tc; cs++){
        cout << "Case #" << cs << ": ";
        solve();
    }


    return 0;
}
