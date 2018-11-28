#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <functional>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <map>
#include <queue>
#include <utility>
#include <vector>

using namespace std;

typedef long long Long;
#define whole(xs) xs.begin(), xs.end()

ostream& operator<<(ostream& os, const vector<int>& v) {
    for (int i = 0; i < v.size(); i++) {
        os << v[i] << " ";
    }
    return os;
}

int N, X;
vector<int> S;
void input() {
    cin >> N >> X;
    S.resize(N, 0);
    for (int i = 0; i < N; i++) {
        cin >> S[i];
    }
}

void solve() {
    sort(whole(S));
    int n = 0;
    bool used[N]; memset(used, 0, sizeof(used));
    for (int i = 0; i < N; i++) {
        if (used[i]) continue;
        n++;
        used[i] = true;
        if (i + 1 == N) continue;
        int last = N;
        for (int j = N - 1; j >= i + 1; j--) {
            if (used[j]) continue;
            if (S[i] + S[j] <= X) {
                last = j;
                break;
            }
        }
        if (last != N) {
            used[last] = true;
        }
    }
    cout << n << endl;
}

int main() {
    int T; cin >> T;
    for (int t = 1; t <= T; t++) {
        cerr << "Case #" << t << endl;
        input();
        cout << "Case #" << t << ": ";
        solve();
    }
    return 0;
}
