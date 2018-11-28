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
#include<complex>
//#include<memory>
#include<functional>
#include<cassert>
#include<set>
#include<stack>
#include<random>

const int dx[] = {1, 0, -1, 0};
const int dy[] = {0, 1, 0, -1};
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int, int> pii;

int cycle[100];

bool ok(int n, const vi& bff) {
    for (int i = 0; i < n; i++) {
        int ni = (i+1)%n;
        int bi = (i+n-1)%n;
        if (bff[cycle[i]] != cycle[ni] && bff[cycle[i]] != cycle[bi]) return false;
    }
    return true;
}

void solve() {
    int N;
    cin >> N;
    vi bff(N);
    for (int i = 0; i < N; i++) {
        cin >> bff[i];
        bff[i]--;
    }
    vi perm(N);
    for (int i = 0; i < N; i++) perm[i] = i;
    int ans = 0;
    do {
        for (int i = ans+1; i <= N; i++) {
            for (int j = 0; j < i; j++) cycle[j] = perm[j];
            if (ok(i, bff)) ans = max(ans, i);
        }
    } while (next_permutation(perm.begin(), perm.end()));
    cout << ans << endl;
}

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": " ;
        solve();
    }
    return 0;
}
