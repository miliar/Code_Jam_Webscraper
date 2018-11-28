
#include<set>
#include<map>
#include<cmath>
#include<queue>
#include<iomanip>
#include<cstdio>
#include<vector>
#include<string>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

#define mem(a, b) (memset(a, b, sizeof(a)))
#define pb push_back
#define all(v) v.begin(), v.end()
#define rall(v) v.rbegin(), v.rend()
#define rep(i, m) for (int i = 0; i < (int)(m); i++)
#define rep2(i, n, m) for (int i = n; i < (int)(m); i++)
typedef long long LL;
typedef pair<int, int> PII;
typedef pair<LL, LL> PLL;

const int oo = (int) 1e9;
const double eps = 1e-9;

int K, L, S;
string s, t;
int sum, kind, mmax;
void dfs(int cur, string &stmp) {
    if (cur == S) {
        ++kind;
        int tmp = 0;
        for (int i = 0; i <= S-L; ++i) {
            if (stmp.substr(i, L) == t) {
                ++tmp;
            }
        }
        sum += tmp;
        mmax = max(mmax, tmp);
        return ;
    }
    for (int i = 0; i < K; ++i) {
        stmp.push_back(s[i]);
        dfs(cur + 1, stmp);
        stmp.pop_back();
    }
}

int main(void) {
    int T, cas = 1;
    cin >> T;
    while (T-- > 0) {
        cin >> K >> L >> S;
        cin >> s;
        cin >> t;

        sum = kind = mmax = 0;
        string stmp = "";
        dfs(0, stmp);
        printf("Case #%d: %.6f\n", cas++, mmax - (0.0 + sum) / kind);
    }
    return 0;
}
