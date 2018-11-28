#include <bits/stdc++.h>
#define INF 0x3f3f3f3f
#define For(i,a,b) for(int (i)=(a);(i) < (b); ++(i))
#define mk make_pair
#define pb push_back
#define fi first
#define se second

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<bool> vb;
const int N = 110;
string grid[N];
int vis[N][N];
char dm[] = {'>', 'v', '<', '^' };
int indd(char x) {
        for(int i = 0;i <4; i++)
                if( x == dm[i])return i;
        return 0;
}

int n, m;
int d[4][2] = {{0,1}, {1,0}, {0,-1}, {-1,0}};
bool impo;

int ans;

int main(){
        ios::sync_with_stdio(false);
        int t,ca=1;
        cin >> t;
        while(t--)
        {
                cin >> n >> m;
                For(i,0,n) cin >> grid[i];
                cout << "Case #" << ca++ << ": " ;
                if( n == 1 && m == 1 )
                {
                        if( grid[0][0] != '.' )
                        {
                                cout << "IMPOSSIBLE\n";
                        }
                        else cout << "0\n";
                        continue;
                }

                impo = false;
                ans=0;
                For(i,0,n)
                {
                        int cnt=0, ind=-1;
                        For(j,0,m)
                        {
                                if( grid[i][j] == '.' )continue;
                                int dd = indd( grid[i][j] );
                                int ui = i, uj = j;

                                bool bad = true;
                                For(k,0,4) {
                                        int vi = i + d[k][0];
                                        int vj = j + d[k][1];
                                        while( vi < n && vi >= 0 && vj < m && vj >= 0)
                                        {
                                                bad &= grid[vi][vj] == '.';
                                                vi = vi + d[k][0];
                                                vj = vj + d[k][1];
                                        }
                                }

                                if( bad ) impo = true;
                                if(impo)break;

                                ui = i+d[dd][0];
                                uj = j+d[dd][1];
                                bad = true;
                                while( ui >= 0 && uj>=0 && ui < n && uj < m )
                                {
                                        bad &= grid[ui][uj] == '.';
                                        ui += d[dd][0];
                                        uj += d[dd][1];
                                }

                                if(bad)
                                        ans++; 
                        }

                }

                if( impo )
                        cout << "IMPOSSIBLE\n";
                else cout << ans << "\n";
        }

        return 0;
}
