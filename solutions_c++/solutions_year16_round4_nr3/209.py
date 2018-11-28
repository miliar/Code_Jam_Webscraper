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
#define pii pair < int, int >


using namespace std;


typedef long long LL;

const int MAXN = 20;

int mat[MAXN][MAXN];


typedef pair < pii, bool > pib;
vector < vector < int > > g;


void dfs(int v, vector < int > & used) {
    used[v] = 1;
    for (int i = 0; i < (int) g[v].size(); ++i) {
        int to = g[v][i];
        if (used[to]) continue;
        dfs(to, used);
    }
}


int cnt = 0;

int gn(pib &p, map < pib, int > &mp) {
    if (mp.find(p) == mp.end()) {
        mp[p] = cnt;
        ++cnt;
        return mp[p];
    }
    return mp[p];
}


int main() {
    int t;
    cin >> t;
    for (int q = 0; q < t; ++q) {
        cerr << q << endl;
        cnt = 0;
        cout << "Case #" << q + 1 << ":\n";
        int n, m;
        cin >> n >> m;
        vector < pii > ps (n + m);
        vector < pib > toP (2 * (n + m));
        for (int i = 0; i < (n + m); ++i) {
            cin >> ps[i].ff >> ps[i].ss;
            --ps[i].ff, --ps[i].ss;
        }

        for (int i = 0; i < m; ++i) {
            toP[i] = mapa(mapa(0, i), true);
        }

        for (int i = 0; i < n; ++i) {
            toP[m + i] = mapa(mapa(i, m), false);
        }

        for (int i = 0; i < m; ++i) {
            toP[m + n + i] = mapa(mapa(n, m - i - 1), true);
        }

        for (int i = 0; i < n; ++i) {
            toP[n + m + m + i] = mapa(mapa(n - i - 1, 0), false);
        }

        
        /*
        for (int i = 0; i < 2 * (n + m); ++i) {
            cout << toP[i].ff.ff << " " << toP[i].ff.ss << " " << toP[i].ss << endl;
        }
        */
        map < pair < pii, bool >, int > mp;
        
        bool gflag = false;
        for (int masc = 0; masc < (1 << (n * m)); ++masc) {
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < m; ++j) {
                    if (masc & (1 << (i * m + j))) {
                        mat[i][j] = 1;
                    }
                    else {
                        mat[i][j] = 0;
                    }
                }
            }
            
            g.clear();
            g.resize((n * m + n + m) * 3);

            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < m; ++j) {
                    pib cp;
                    cp.ff = mapa(i, j);
                    cp.ss = true;
                    pib scp = cp;
                    scp.ss = false;
                    if (mat[i][j] == 0) {                        
                        //cout << "lol" << endl;
                        g[gn(cp, mp)].puba(gn(scp, mp));
                        g[gn(scp, mp)].puba(gn(cp, mp));
                        //cout << gn(cp, mp) << " " << gn(scp, mp) << endl; 
                        cp.ff.ff += 1;
                        scp.ff.ss += 1;

                        //cout << gn(cp, mp) << " " << gn(scp, mp) << endl;
                        g[gn(cp, mp)].puba(gn(scp, mp));
                        g[gn(scp, mp)].puba(gn(cp, mp));
                    }
                    else {
                        pib tmp = scp;
                        tmp.ff.ss += 1;
                        g[gn(cp, mp)].puba(gn(tmp, mp));   
                        g[gn(tmp, mp)].puba(gn(cp, mp));
                    
                        tmp = cp;
                        tmp.ff.ff += 1;
                        g[gn(scp, mp)].puba(gn(tmp, mp));   
                        g[gn(tmp, mp)].puba(gn(scp, mp));
                    }
                }
            }

            /*
            for (map < pib, int >::iterator it = mp.begin(); it != mp.end(); ++it) {
                pib p = (*it).ff;
                cout << p.ff.ff << " " << p.ff.ss << " " << p.ss << "   " << (*it).ss << endl;
            }
            cout << "#" << endl;

            for (int i = 0; i < cnt; ++i) {
                for (int j = 0; j < (int) g[i].size(); ++j) {
                    cout << g[i][j] << " ";
                }
                cout << endl;
            }
            
            //cout << "@" << endl;
            */
            bool flag = true;
            vector < int > used (cnt + 1, 0);

            for (int i = 0; i < m + n; ++i) {
                
                int ff = gn(toP[ps[i].ff], mp);
                int ss = gn(toP[ps[i].ss], mp);
                if (used[ff] || used[ss]) {
                    flag = false;
                    break;
                }

                dfs(ff, used);
                if (!used[ss]) {
                    flag = false;
                    break;
                }
            }

            if (!flag) {
                continue;
            }

            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < m; ++j) {
                    if (mat[i][j] == 0) cout << '/';
                    else cout << "\\";
                }
                cout << "\n";
            }
            gflag = true;
            break;
        }

        if (!gflag) {
            cout << "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}