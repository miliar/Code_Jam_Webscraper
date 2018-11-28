#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

using namespace std;

typedef long double real;


real memo[201][201][401];
real p[201];
real used[201];
real pyes[201][201];
int rk;

void bf(int n, int k, real& sol){
    if(k == 0){
        memset(pyes, 0, sizeof(pyes));
        pyes[0][0] = 1.0;
        for(int i = 1; i <= rk; i++){
            pyes[i][0] = (1 - used[i - 1]) * pyes[i - 1][0];
            for(int x = 1; x <= i; x++){
                pyes[i][x] = used[i - 1] * pyes[i - 1][x - 1] + (1 - used[i - 1]) * pyes[i - 1][x];

            }
        }

        
        sol = max(sol, pyes[rk][rk / 2]);
        return;
    }
    if(n == 0) return;

    used[k - 1] = p[n - 1];
    bf(n - 1, k - 1, sol);
    bf(n - 1, k, sol);
}


int main(){
    //ios::sync_with_stdio(false);

    int T;
    cin >> T;

    for(int tc = 1; tc <= T; tc++){
        int n, k;
        cin >> n >> k;

        for(int i = 0; i < n; i++) cin >> p[i];

        real sol = 0.0;
        rk = k;
        bf(n, k, sol);

        cout << "Case #" << tc << ": ";
        cout << fixed << setprecision(9) << sol << '\n';
    }
}
