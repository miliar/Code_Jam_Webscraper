#include <iostream>
#include <cstdio>
#include <vector>
#include <ctime>
#include <cstdlib>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <unordered_map>
#include <unordered_set>
#include <cstring>


#define puba push_back
#define mapa make_pair
#define ff first
#define ss second
#define pii piar < int, int >


using namespace std;


typedef long long LL;
typedef long double LD;


const int MAXN = 220;


LD dp[MAXN][MAXN];


int main() {
    int t;
    cin >> t;
    for (int q = 0; q < t; ++q) {
        cout << "Case #" << q + 1 << ": ";
        int n, k;
        cin >> n >> k;
        vector < LD > ps (n);
        for (int i = 0; i < n; ++i) {
            cin >> ps[i];
        }

        sort(ps.begin(), ps.end());
        /*
        for (int i = 0; i < n; ++i) {
            cout << ps[i] << " ";
        }
        cout << endl;
        */
        LD ans = 0.0;
        vector < LD > vans;

        for (int num = 0; num <= k; ++num) {
            vector < LD > nps;
            for (int j = 0; j < num; ++j) {
                nps.puba(ps[j]);
            }
            for (int j = 0; j < k - num; ++j) {
                nps.puba(ps[ps.size() - 1 - j]);
            }

            for (int i = 0; i < MAXN; ++i) {
                for (int j = 0; j < MAXN; ++j) {
                    dp[i][j] = 0.0;
                }
            }
            dp[0][0] = 1.0;
            for (int i = 1; i <= k; ++i) {
                for (int j = 0; j <= i; ++j) {
                    if (j == 0) {
                        dp[i][0] = (1.0 - nps[i - 1]) * dp[i - 1][j];    
                        continue;
                    }
                    dp[i][j] = nps[i - 1] * dp[i - 1][j - 1] + (1.0 - nps[i - 1]) * dp[i - 1][j];
                }
            }
            if (ans < dp[k][k / 2]) {
                ans = dp[k][k / 2];
                //vans = nps;
            }
        }
        /*
        for (int masc = 0; masc < (1 << n); ++masc) {
            vector < LD > nps;
            int cnt = 0;
            for (int i = 0; i < n; ++i) {
                if (masc & (1 << i)) {
                    ++cnt;
                    nps.puba(ps[i]);
                }
            }
            if (cnt != k) continue;

            
            //ans = max(ans, dp[k][k / 2]);
        }
        for (int i = 0; i < (int) vans.size(); ++i) {
           cout << vans[i] << " "; 
        }
        cout << endl;

        */
        cerr << q << endl;
        printf("%.10f\n", (double) ans);
        
    }
    return 0;
}