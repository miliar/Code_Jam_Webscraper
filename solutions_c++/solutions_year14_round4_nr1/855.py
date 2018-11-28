
#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <utility>
#include <vector>
#define MAXN 10000

using namespace std;

int N, X;
int s[MAXN];

void solve() {
    cin >> N >> X;
    for (int i = 0; i < N; i++)
        cin >> s[i];
    sort(s, s + N);

    int total = 0;
    int i = 0;
    for (int j = N - 1; j >= i; j--) {
        total++;
        if (j > i && s[i] + s[j] <= X)
            i++;
    }

    cout << total << endl;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";
        solve();
    }
}

