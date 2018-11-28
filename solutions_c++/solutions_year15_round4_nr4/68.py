#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef stringstream ss;

#define sz(x) ((int)(x).size())
#define all(x) (x).begin(),(x).end()
#define mset(t,v) memset((t),(v),sizeof(t))
#define print(a) cout << #a << ": " << a << endl;
#define print_arr(a,n) rep(_##i, n) cout << #a << "[" << _##i << "]: " << a[_##i] << endl

#define rep(i,n) for(int i=0,_##i=(n);i<_##i;++i)
#define repr(i,n) for(int i=(n);--i>=0;)
#define rep2(i,l,r) for(int i=(l),_##i=(r);i<_##i;++i)
#define repr2(i,l,r) for(int i=(r),_##i=(l);--i>=_##i;)

#define vt(args...) vector<tuple<args>>
#define mp make_pair
#define pb push_back
#define eb emplace_back
#define em emplace

const long long MOD = 1000000007;
long long dp1[105];
long long dp4[105];
long long dp3[105];
long long dp6[105];
long long dp12[105];

int R;
int C;

long long get1(int i) {
    if (i == -2) return 1;
    if (i < 0) return 0;
    return dp1[i];
}

long long get4(int i) {
    if (i < 0) return 0;
    return dp4[i];
}

long long get3(int i) {
    if (i < 0) return 0;
    return dp3[i];
}

long long get6(int i) {
    if (i < 0) return 0;
    return dp6[i];
}

long long get12(int i) {
    if (i < 0) return 0;
    return dp12[i];
}

long long mypow(long long b, long long e) {
    if (e == 0) return 1;
    long long tmp = mypow(b, e / 2);
    tmp = (tmp * tmp) % MOD;
    if (e & 1) {
        tmp = (tmp * b) % MOD;
    }
    return tmp;
}

long long myinv(long long b) {
    long long ret = mypow(b, MOD - 2);
    assert((ret * b) % MOD == 1);
    return ret;
}

long long get_ans(int i) {
    long long ret = 0;
    ret = dp1[i];
    ret += (dp3[i] * myinv(3)) % MOD;
    ret += (dp4[i] * myinv(4)) % MOD;
    ret += (dp6[i] * myinv(6)) % MOD;
    ret += (dp12[i] * myinv(12)) % MOD;
    return ret % MOD;
}

void solve_case(int i) {
    cout << "Case #" << i << ": ";
    cin >> R >> C;
    dp1[0] = 1;
    dp3[0] = 0;
    dp4[0] = 0;
    dp6[0] = 0;
    dp12[0] = 0;
    rep2(i, 1, R + 1) {
        dp1[i] = 0;
        dp3[i] = 0;
        dp4[i] = 0;
        dp6[i] = 0;
        dp12[0] = 0;

        dp1[i] += get1(i - 3);
        dp3[i] += get3(i - 3);
        dp4[i] += get4(i - 3);
        dp6[i] += get6(i - 3);
        dp12[i] += get12(i - 3);

        if (C % 4 == 0) {
            dp4[i] += 4 * get1(i - 5);
            dp4[i] += 4 * get4(i - 5);
            dp12[i] += 4 * get3(i - 5);
            dp12[i] += 4 * get6(i - 5);
            dp12[i] += 4 * get12(i - 5);
        }
        
        if (C % 3 == 0) {
            dp3[i] += 3 * get1(i - 4);
            dp3[i] += 3 * get3(i - 4);
            dp12[i] += 3 * get4(i - 4);
            dp6[i] += 3 * get6(i - 4);
            dp12[i] += 3 * get12(i - 4);
        }

        if (C % 6 == 0) {
            dp6[i] += 6 * get1(i - 4);
            dp6[i] += 6 * get3(i - 4);
            dp12[i] += 6 * get4(i - 4);
            dp6[i] += 6 * get6(i - 4);
            dp12[i] += 6 * get12(i - 4);
        }

        dp1[i] %= MOD;
        dp3[i] %= MOD;
        dp4[i] %= MOD;
        dp6[i] %= MOD;
        dp12[i] %= MOD;
    }
    long long ans = (get_ans(R) + get_ans(R - 2)) % MOD;
    cout << ans << "\n";
}

int main(){
    int T;
    cin >> T;
    rep(i, T) solve_case(i + 1);
    return 0;
}

