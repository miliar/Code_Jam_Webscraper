#include <cstdio>
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
#include <numeric>
#include <climits>
#include <cfloat>
#include <functional>
using namespace std;

const int INF = INT_MAX / 2;

int solve()
{
    int p, q, n;
    cin >> p >> q >> n;
    vector<int> hp(n), gold(n);
    for(int i=0; i<n; ++i)
        cin >> hp[i] >> gold[i];

    vector<bool> isKill(201, false);
    for(int i=0; i<=p; ++i)
        isKill[i] = true;
    for(int i=1; i+p+q<=200; ++i)
        isKill[i+p+q] = isKill[i];

    vector<vector<int> > dp(2, vector<int>(11000, -INF));
    dp[0][0] = 0;
    for(int i=0; i<n; ++i){
        vector<vector<int> > nextDp(2, vector<int>(11000, -INF));
        for(int j=0; j<=10000; ++j){
            // æ§UŒ‚‚ð‰Á‚¦‚Ä‚¨‚¢‚½ê‡
            for(int k=0; k<=min(j,200); ++k){
                if(k * p >= hp[i]){
                    nextDp[0][j-k] = max(nextDp[0][j-k], dp[0][j] + gold[i]);
                    nextDp[1][j-k] = max(nextDp[1][j-k], dp[1][j] + gold[i]);
                    continue;
                }

                int hp2 = hp[i] - k * p;
                if(isKill[hp2])
                    nextDp[1][j-k] = max(nextDp[1][j-k], dp[0][j] + gold[i]);

                if(q < hp[i] - k * p){
                    int hp3 =  hp[i] - k * p - q;
                    if(isKill[hp3])
                        nextDp[1][j-k] = max(nextDp[1][j-k], dp[1][j] + gold[i]);
                }
            }

            // ‘¼‚Ì“G‚Éæ§UŒ‚‚ð‰Á‚¦‚éê‡
            int hp2 = hp[i];
            for(int k=0; hp2 > 0; ++k){
                if(isKill[hp2])
                    nextDp[1][j+k] = max(nextDp[1][j+k], dp[0][j] + gold[i]);
                nextDp[0][j+k+1] = max(nextDp[0][j+k+1], dp[0][j]);
                hp2 -= q;
            }

            if(q > hp[i]){
                nextDp[0][j] = max(nextDp[0][j], dp[1][j]);
            }
            else{
                int hp3 = hp[i] - q;
                for(int k=0; hp3 > 0; ++k){
                    if(isKill[hp3])
                        nextDp[1][j+k] = max(nextDp[1][j+k], dp[1][j] + gold[i]);
                    nextDp[0][j+k+1] = max(nextDp[0][j+k+1], dp[1][j]);
                    hp3 -= q;
                }
            }
        }
        dp.swap(nextDp);
    }

    int ret = -INF;
    for(int i=0; i<2; ++i)
        ret = max(ret, *max_element(dp[i].begin(), dp[i].end()));
    return ret;
}

int main()
{
    int T;
    cin >> T;

    for(int tc=1; tc<=T; ++tc){
        int ret = solve();
        cout << "Case #" << tc << ": " << ret << endl;
    }

    return 0;
}