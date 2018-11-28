#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

void read();
void kill();

int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cout.precision(11);
    cout << fixed;
    int t;

    cin >> t;

    for (int i = 1; i <= t; ++i){
        read();
        cout << "Case #" << i << ": ";
        kill();
    }

    return 0;
}

#define long long long

#define M 239
#define T 2014
#define INF 1000000000

int p, q, n, d[M][T], t[M][T];
int h[M], g[M];


void read(){
    cin >> p >> q >> n;
    for (int i = 1; i <= n; ++i)
        cin >> h[i] >> g[i];
}


void kill(){
    for (int i = 0; i <= n; ++i)
    for (int j = 0; j < T; ++j)
        d[i][j] = t[i][j] = -INF;

    d[0][0] = 0;
    t[0][1] = 0;
    t[0][0] = 0;


    for (int i = 1; i <= n; ++i)
        for (int j = 0; j < T; ++j){
            d[i][j] = -INF;
            t[i][j] = -INF;

            int my = (h[i] + p - 1) / p;
            if (j + my < T){
                d[i][j] = max(d[i][j], d[i - 1][j + my] + g[i]);
                t[i][j] = max(t[i][j], t[i - 1][j + my] + g[i]);
            }

            int tow = (h[i] + q - 1) / q;
            d[i][j] = max(d[i][j], d[i - 1][max(j - tow, 0)]);
            t[i][j] = max(t[i][j], t[i - 1][max(j - tow, 0)]);

            tow = tow - 1;
            if (tow == 0)
                continue;

            int steps = (h[i] - q*tow + p - 1) / p;
            if (j - tow + steps < T){
                t[i][j] = max(t[i][j], d[i - 1][max(j - tow + steps - 1, 0)] + g[i]);
                t[i][j] = max(t[i][j], t[i - 1][max(j - tow + steps, 0)] + g[i]);
            }
        }

    int ans = 0;
    for (int i = 0; i < T; ++i)
        ans = max(t[n][i], ans);
    cout << ans << "\n";
}
