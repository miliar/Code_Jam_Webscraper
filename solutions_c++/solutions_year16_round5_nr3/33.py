#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <sstream>
#include <cmath>
#include <iomanip>
using namespace std;

int tests, n, s;
int x[1010], y[1010], z[1010], vx[1010], vy[1010], vz[1010];
int dist[1010];
bool vis[1010];

int sqr(int i) {
    return i * i;
}

int calc(int i, int j) {
    return sqr(x[i] - x[j]) + sqr(y[i] - y[j]) + sqr(z[i] - z[j]);
}

int main() {
    cin >> tests;
    cout << std::fixed << setprecision(9);
    for (int cases = 1; cases <= tests; ++ cases) {
        cin >> n >> s;
        for (int i = 0; i < n; ++ i)
            cin >> x[i] >> y[i] >> z[i] >> vx[i] >> vy[i] >> vz[i];
        for (int i = 0; i < n; ++ i) {
            vis[i] = false;
            dist[i] = calc(0, i);
        }
        vis[0] = true;
        dist[0] = 2000000000;
        int ans = 0;
        while (vis[1] == false) {
            int m = 0;
            for (int i = 1; i < n; ++ i) {
                if (vis[i]) continue;
                if (dist[i] < dist[m])
                    m = i;
            }
            ans = max(ans, dist[m]);
            vis[m] = true;
            for (int i = 1; i < n; ++ i) {
                if (vis[i]) continue;
                dist[i] = min(dist[i], calc(i, m));
            }
        }
        cout << "Case #" << cases << ": " << sqrt(ans) << endl;
    }
    return 0;
}
