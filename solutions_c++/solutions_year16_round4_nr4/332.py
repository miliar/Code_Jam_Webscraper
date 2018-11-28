#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
//#include<cctype>
#include<climits>
#include<iostream>
#include<string>
#include<vector>
#include<map>
//#include<list>
#include<queue>
#include<deque>
#include<algorithm>
//#include<numeric>
#include<utility>
//#include<memory>
#include<functional>
#include<cassert>
#include<set>
#include<stack>
#include<random>

const int dx[] = {1, 0, -1, 0};
const int dy[] = {0, -1, 0, 1};
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int, int> pii;

inline int at(int flag, int worker, int machine, int N) {
    int index = worker*N+machine;
    return (flag>>index)&1;
}

bool ok(int flag, int N) {
    vector<int> perm(N);
    for (int i = 0; i < N; i++)
        perm[i] = i;
    for (int i = 0; i < N; i++) {
        if (((flag>>(N*i))&((1<<N)-1)) == 0) return false;
        sort(perm.begin(), perm.end());
        bool ok = true;
        do {
            bool ng = false;
            for (int j = 0; j < N; j++) {
                if (perm[j] == i && at(flag, i, j, N)) {
                    ng = true;
                    break;
                }
                if (perm[j] == i) continue;
                if (!at(flag, i, j, N)) continue;
                if (!at(flag, perm[j], j, N)) {
                    ng = true;
                    break;
                }
            }
            if (!ng) {
                ok = false;
                break;
            }
        } while (next_permutation(perm.begin(), perm.end()));
        if (!ok) return false;
    }
    return true;
}

void solve() {
    int N;
    cin >> N;
    int flag = 0;
    for (int i = 0; i < N; i++) {
        string s;
        cin >> s;
        int tmp = 0;
        for (int j = 0; j < N; j++) if (s[j] == '1') {
            tmp |= 1<<j;
        }
        flag |= tmp<<(i*N);
    }
    int ans = N*N;
    for (int s = 0; s < 1<<(N*N); s++) {
        if (ans <= __builtin_popcount(s)) continue;
        if (flag&s) continue;
        int nflag = s | flag;
        if (ok(nflag, N)) ans = __builtin_popcount(s);
    }
    cout << ans << endl;
}

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";
        solve();
    }
    return 0;
}
