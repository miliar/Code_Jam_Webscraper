#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <map>
#include <climits>
using namespace std;

#define REP(i,n) for(int i=0; i<(int)(n); i++)
#define RREP(i,n) for(int i=(int)n-1; i>=0; i--)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define RFOR(i,c) for(__typeof((c).rbegin())i=(c).rbegin();i!=(c).rend();++i)
#define ALL(c) (c).begin(), (c).end()

typedef long long int ll;
typedef pair<int, int> pii;
typedef pair<int, pair<int, int> > pipii;
typedef vector<int> vi;

const int INF = 10000000;
const int MOD = 1e9+7;

int dp[1100][1100];

int main(void){
	int T;
    cin >> T;
    REP(i, 100){
        REP(j, 100){
            dp[i][j] = INF;
            if(i <= j) dp[i][j] = 0;
            for(int k = 1; k <= i/2; k++){
                dp[i][j] = min(dp[i][j], dp[k][j] + dp[i-k][j] + 1);
            }
        }
    }
    REP(tt, T){
        int D;
        cin >> D;
        vi p;
        REP(i, D){
            int x;
            cin >> x;
            p.push_back(x);
        }
        int ans = INF;
        for(int i = 1; i <= 50; i++){
            int x = 0;
            REP(j, D){
                x += dp[p[j]][i];   
            }
            ans = min(ans, x + i);
        }
        cout << "Case #" << tt + 1 << ": ";
        cout << ans << endl;
    }
	
	return 0;
}

