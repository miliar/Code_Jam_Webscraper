// In the name of God

#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <deque>
#include <assert.h>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <stdio.h>
#include <string.h>
#include <utility>
#include <math.h>
#include <bitset>
#include <iomanip>

using namespace std;

#define rep(i, n) for (int i = 0, _n = (int)(n); i < _n; ++i)
/*
#define cin fin
*/
#define cout fout

//ifstream fin(".in");
ofstream fout("res.out");

const int N = 1 << 13, M = 13, mod = 0;

//0 p 1 r 2 s
string res[M][N];
int win[3];


int main() {
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int tc;
    cin >> tc;
    rep(ntc, tc) {
        cout << "Case #" << ntc + 1 << ": ";
        // Clear Start
        
        // Clear End
        // Start
        int n, r, p, s;
        cin >> n >> r >> p >> s;
        res[0][0] = "PR"; win[0] = 1;
        res[0][1] = "RS"; win[1] = 2;
        res[0][2] = "PS"; win[2] = 0;
        for (int g = 1; g < n; ++g)
            for (int i = 0; i < 3; ++i) {
                if (res[g - 1][win[i]] > res[g - 1][i]) {
                    res[g][i] = res[g - 1][i];
                    res[g][i] += res[g - 1][win[i]];
                } else {
                    res[g][i] = res[g - 1][win[i]];
                    res[g][i] += res[g - 1][i];
                }
            }
        string ans = "IMPOSSIBLE";
        for (int w = 0; w < 3; ++w) {
            int cr = 0, cp = 0, cs = 0;
            for (int i = 0; i < res[n - 1][w].size(); ++i) {
                cr += (res[n - 1][w][i] == 'R');
                cp += (res[n - 1][w][i] == 'P');
                cs += (res[n - 1][w][i] == 'S');
            }
            if (cr == r && cp == p && cs == s && (ans == "IMPOSSIBLE" || ans > res[n - 1][w]))
                ans = res[n - 1][w];
        }   
        // End
        cout << ans << '\n';
    }
}













