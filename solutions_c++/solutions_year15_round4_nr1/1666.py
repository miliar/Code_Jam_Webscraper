#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <sstream>
#include <cmath>
#include <ctime>
#include <memory.h>

#define WR printf
#define RE scanf
#define PB push_back
#define SE second
#define FI first
#define MP make_pair

#define FOR(i,Be,En) for(int (i)=(Be);(i)<=(En);++(i))
#define DFOR(i,Be,En) for(int (i)=(Be);(i)>=(En);--(i))
#define SZ(a) (int)((a).size())
#define FA(i,v) FOR(i,0,SZ(v)-1)
#define RFA(i,v) DFOR(i,SZ(v)-1,0)
#define CLR(a) memset(a,0,sizeof(a))

#define LL  long long
#define VI  vector<int>
#define PAR pair<int ,int> 

using namespace std;
void __never(int a){printf("\nOPS %d", a);}
void __die(int a){printf("%d",(a*a)/(a+a));}
#define ass(s) ;//{if (!(s)) {__never(__LINE__);cout.flush();cerr.flush();__die(0);}}


#define MN 128


bool bad[MN][MN];


int dx[] = {-1,0,1,0};
int dy[] = {0,1,0,-1};


std::string di = "^>v<";

int opp(int a) {
    return ((a + 2) & 3);
}


int dir(char c) {
    if (c == '^') return 0;
    if (c == '>') return 1;
    if (c == 'v') return 2;
    if (c == '<') return 3;
    return 4;
}

void init()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
}

int sol() {
    int n, m;
    cin >> n >> m;
    std::vector<std::string> g(n);
    FOR(i,0,n-1) cin >> g[i];
    CLR(bad);
   
   
    FOR(i,0,n-1) {
        FOR(j,0,m-1) {
            int d = dir(g[i][j]);
            if (d == 4) continue;
            int x = i, y = j;
            while (true) {
                x += dx[d];
                y += dy[d];
                if (x >= n || x < 0 || y >=m || y < 0) {
                    bad[i][j] = true;
                    break;
                }
                if (g[x][y] != '.') break;
                
                
            }
        }
    }
    
    int ans = 0;
    FOR(i,0,n-1) FOR(j,0,m-1) if (bad[i][j]){
        int r = 3;
        int dd = -1;
        int xx, yy;
        FOR(d,0,3) {
            int x = i, y = j;
            while (true) {
                x += dx[d];
                y += dy[d];
                if (x >= n || x < 0 || y >=m || y < 0) break;
                if (g[x][y] == '.') continue;
                
                if (d == opp(g[x][y])) { // 0
                    
                    ass(!bad[x][y]);
                    if (r > 0) {
                        r = 0;
                        dd = d;
                    }
                    break;
                } else if (bad[x][y]){ // 1
                    if (r > 1) {
                        r = 1;
                        dd = d;
                        xx = x;
                        yy = y;
                    }
                    break;
                } else {
                    r = 2;
                    dd = d;
                }
            }
        }
        if (r == 0) {
            bad[i][j] = false;
            g[i][j] = di[dd];
            ans++;
        }
        if (r == 1) {
            bad[i][j] = false;
            ass(bad[xx][yy]);
            bad[xx][yy] = false;
            g[i][j] = di[dd];
            g[xx][yy] = di[opp(dd)];
            ans += 2;
        }
        if (r == 2) {
            bad[i][j] = false;
            g[i][j] = di[dd];
            ans++;
        }
        if (r == 3) {
            return -1;
        }
    }
    return ans;
}
int main()
{
	init();
    int T;
    cin >> T;
    int ans = 0;
    FOR(t,1,T) {
        ans = sol();
        std::cout << "Case #" << t << ": ";
        if (ans == -1) cout << "IMPOSSIBLE";
        else cout << ans;
        cout <<"\n";
    }
	return 0;
}