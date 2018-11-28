#include <iostream>
#include <cstdio>
#define INF 1000000000

using namespace std;

void solve(int caseNumber) {
    double c, f, x;
    cin >> c >> f >> x;
    double factoriesBuilt[1000000] = {0};
    factoriesBuilt[0] = 0;
    double time = INF;
    for (int i = 0; i < 50001; i++) {
        time = min(time, factoriesBuilt[i] + (x / (2 + f * i)));
        factoriesBuilt[i + 1] = factoriesBuilt[i] + (c / (2 + f * i));
    }
    printf("Case #%d: %.7lf\n", caseNumber, time);
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int i = 0; i < T; i++)
        solve(i + 1);
    return 0;
}
