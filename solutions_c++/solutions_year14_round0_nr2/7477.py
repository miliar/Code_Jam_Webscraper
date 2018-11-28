#include <bits/stdc++.h>
#define msg(x) cout << #x << " = " << x << endl
using namespace std;

int t;
double C, F, X;

int main() {
    cin.sync_with_stdio(0); cin.tie(0);
    freopen("output.txt", "w", stdout);
    cin >> t;
    cout.precision(7);
    for (int tc = 1; tc <= t; tc++) {
        cin >> C >> F >> X;
        double best = X * 0.5;
        double sum = 0, tmp;
        for (int i = 0; i < 100224; i++) {
            sum += C / (2 + i * F);
            tmp = sum + X / (2 + F * (i + 1));
            best = min(best, tmp);
        }
        cout << "Case #" << tc << ": ";
        cout << fixed << best;
        cout << "\n";
    }
    return 0;
}
