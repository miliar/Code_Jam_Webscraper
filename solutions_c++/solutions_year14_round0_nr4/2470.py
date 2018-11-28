#include <iostream>
#include <fstream>
#include <set>
#include <string.h>
#include <algorithm>

using namespace std;

double N[1002];
double K[1002];
set <double> Ks;

int t;
void solve() {
    printf("Case #%d: ", t);
    int n, i, j, mn, b, s1 = 0, s2 = 0;
    cin >> n;
    for (i = 0; i < n; ++i) cin >> N[i];
    Ks.clear();
    for (i = 0; i < n; ++i) {
        cin >> K[i];
        Ks.insert(K[i]);
    }
    sort(N, N + n);
    sort(K, K + n);
    //cerr << "N: ";
    //for (i = 0; i < n; ++i) cerr << N[i] << " ";
    //cerr << "\nK: ";
    //for (i = 0; i < n; ++i) cerr << K[i] << " ";
    //cerr << "\n";
    for (i = 0; i < n; ++i) {
        if (*Ks.begin() < N[i]) {
            Ks.erase(Ks.begin());
            s1++;
        }
    }
    for (i = 0; i < n; ++i) {
        for (mn = 0, j = 1; j < n; ++j) if (K[mn] > K[j]) mn = j;;
        for (b = 0; b < n && (K[b] == 2 || K[b] < N[i]); ++b);
        if (b == n) {
            s2++;
            K[mn] = 2;
        }
        else {
            K[b] = 2;
        }
    }
    printf("%d %d\n", s1, s2);
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    scanf("%d", &T);
    for (t = 1; t <= T; ++t) solve();
    return 0;
}