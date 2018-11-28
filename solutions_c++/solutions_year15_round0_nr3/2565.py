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

const int INF = 1e9;
const int MOD = 1e9+7;

int dp[10100][4][4][2];

int main(void){
    int mul[4][4] = {
        {1, 2, 3, 4},
        {2, -1, 4, -3},
        {3, -4, -1, 2},
        {4, 3, -2, -1}
    };
	
    int T;
    cin >> T;
    REP(tt, T){
        memset(dp, 0, sizeof(dp));
        int l, x;
        cin >> l >> x;
        string str;
        cin >> str;
        REP(i, str.size()){
            if(str[i] == 'i') str[i] = '2';
            if(str[i] == 'j') str[i] = '3';
            if(str[i] == 'k') str[i] = '4'; 
        }
        string s = "";
          
        REP(i, x) s += str;
        //cout << s << endl;
        int n = s.size();
        dp[0][0][0][0] = 1;  
        REP(i, n){
            int sid = (int)(s[i] - '0');
            if(!i){
                dp[i+1][0][sid-1][0] = 1;
                if(sid == 2) dp[i+1][1][0][0] = 1; 
            }
            REP(j, 4){
                REP(k, 4){
                    int m = mul[k][sid-1];
                    if(m >= 0){ 
                        //if(!j){
                            dp[i+1][j][m-1][0] |= dp[i][j][k][0];
                            dp[i+1][j][m-1][1] |= dp[i][j][k][1];
                        //}
                        
                        if((m - j) == 2){
                            dp[i+1][j+1][0][0] |= dp[i][j][k][0];
                            dp[i+1][j+1][0][1] |= dp[i][j][k][1];
                        }
                        if(k == 0){
                            dp[i+1][j][m-1][0] |= dp[i][j][k][0];
                            dp[i+1][j][m-1][1] |= dp[i][j][k][1];
                        }
                    }
                    else{
                        //if(!dp[i][j][k][0] && !dp[i][j][k][1]) continue;
/*
                        if(i == 2){
                            cout << "pass" << endl;
                            cout << i << "*" << j << ":" << k << ":";
                            cout << "   " << dp[i][j][k][0] << "*" << dp[i][j][k][1] << endl;
                        }
  */                      
                        
                        //if(!j){
                            dp[i+1][j][-m-1][1] |= dp[i][j][k][0];
                            dp[i+1][j][-m-1][0] |= dp[i][j][k][1];
                        //}

                        if((-m - j) == 2){
                            dp[i+1][j+1][0][1] |= dp[i][j][k][0];
                            dp[i+1][j+1][0][0] |= dp[i][j][k][1];
                        }
                        if(k == 0){
                            dp[i+1][j][-m-1][1] |= dp[i][j][k][0];
                            dp[i+1][j][-m-1][0] |= dp[i][j][k][1];
                        }
                    }
                }
            }
        }
/*
        REP(i, n+1){
            cout << "++++++++" << endl;
            REP(j, 4){
                REP(k, 4){
                    cout << dp[i][j][k][0];
                }cout << endl;
            }cout << endl << endl;
            
            cout << "----------" << endl;
            REP(j, 4){
                REP(k, 4){
                    cout << dp[i][j][k][1];
                }cout << endl;
            }cout << endl << endl;
        }cout << endl;
        */
        cout << "Case #" << tt+1 << ": ";
        if(dp[n][3][0][0]) cout << "YES" << endl;
        else cout << "NO" << endl;
    }

    return 0;
}

