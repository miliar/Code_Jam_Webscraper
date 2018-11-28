
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

int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
string path = ">v<^";

bool check(int x, int y, vector<vector<char> > &m){
    //cout << "x " << x << " y " << y << endl;
    REP(i, 4){
        if(m[x][y] != path[i]) continue;   
        x += dx[i];
        y += dy[i];
        while(1){
            //cout << "pos" << x << ":" << y << endl;
            if(x < 0 || y < 0) return true;
            if(x >= m.size() || y >= m[0].size()) return true;
            if(m[x][y] != '.') return false;
            x += dx[i];
            y += dy[i];
        }
    }
}

int main(void){
    int t;
    cin >> t;
    REP(tt, t){
        int R, C;
        cin >> R >> C;
        vector<vector<char> > m(R, vector<char>(C));
        REP(r, R){
            REP(c, C){
                cin >> m[r][c];
            }
        }
        ll ans = 0;
        int f = 1;
        REP(r, R){
            REP(c, C){
                if(m[r][c] != '.'){
                    if(check(r, c, m)){
                        ans++;
                        char cc = m[r][c];
                        string s = ">v<^";
                        int ff = 0;
                        REP(i, 4){
                            if(s[i] == cc) continue;
                            m[r][c] = s[i];
                            if(!check(r, c, m)){
                                //cout << "path at " << r << ":" << c << endl;
                                ff = 1;
                            }
                        }
                        if(!ff) f = ff;
                        m[r][c] = cc;
                    }
                }
            }
        }
        cout << "Case #" << tt + 1 << ": ";
        if(f) cout << ans << endl;    
        else cout << "IMPOSSIBLE" << endl;
    }
	
	return 0;
}

