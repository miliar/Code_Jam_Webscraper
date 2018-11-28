/* In the name of ALLAH, most gracious, most merciful */

#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <cassert>
#include <set>
#include <ctime>
#include <iomanip>
#include <cstring>
#include <map>
 
using namespace std;
typedef long long ll;
typedef pair< int, int > pi;

int r, c, m;
bool g[10][10];
bool vis[10][10];

char final[10][10];
int totals[10][10];

int floodFill(int rr, int cc){
    if(rr < 0 || rr == r || cc < 0 || cc == c) return 0;
    if(vis[rr][cc] || g[rr][cc]) return 0;
    vis[rr][cc] = true;
    if(totals[rr][cc] != 0) return 1;
    int ret = 1;
    for(int a = -1; a <= 1; a++){
        for(int b = -1; b <= 1; b++){
            if(a == b && a == 0) continue;
            ret += floodFill(rr + a, cc + b);
        }
    }
    return ret;
}

bool solve(int mask, int idx, int count){
    if(idx == r * c){
        if(count != m) return false;
        for(int i = 0; i < idx; i++){
            g[i / c][i % c] = (1 << i) & mask;
        }
        for(int i = 0; i < r; i++){
            for(int j = 0; j < c; j++){
                if(g[i][j]) continue;
                int total = 0;
                for(int a = -1; a <= 1; a++){
                    for(int b = -1; b <= 1; b++){
                        if(a == b && a == 0) continue;
                        if(i + a < 0 || i + a == r || j + b < 0 || j + b == c) continue;
                        total += g[i + a][j + b];
                    }
                }
                totals[i][j] = total;
            }
        }
        for(int i = 0; i < r; i++){
            for(int j = 0; j < c; j++){
                if(!g[i][j]){
                    memset(vis, false, sizeof vis);
                    int val = floodFill(i, j);
                    if(val == r*c - m) {
                        for(int a = 0; a < r; a++){
                            for(int b = 0; b < c; b++){
                                if(g[a][b]){
                                    final[a][b] = '*';
                                }else{
                                    final[a][b] = '.';
                                }
                            }
                        }
                        final[i][j] = 'c';
                        return true;
                    }
                }
            }
        }
        return false;
    }
    bool ret = solve(mask | (1 << idx), idx + 1, count + 1);
    if(ret) return true;
    ret = solve(mask, idx + 1, count);
    return ret;
}

bool ans[10][10][33];

vector< string > grids[10][10][33];

int main()
{
#ifndef ONLINE_JUDGE
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);
#endif
    
    int T;
    cin >> T;
    for(int i = 1; i <= 5; i++){
        for(int j = 1; j <= 5; j++){
            for(int k = 0; k < i * j; k++){
                r = i, c = j, m = k;
                ans[i][j][k] = solve(0, 0, 0);
                if(ans[i][j][k]){
                    for(int a = 0; a < i; a++){
                        grids[i][j][k].push_back("");
                        for(int b = 0; b < c; b++){
                            grids[i][j][k][a] += final[a][b];
                        }
                    }
                }
            }
        }
    }
    
    int i = 4, j = 7, k = 3;
    r = 4, c = 7, m = 3;
    ans[i][j][k] = solve(0, 0, 0);
    if(ans[i][j][k]){
        for(int a = 0; a < i; a++){
            grids[i][j][k].push_back("");
            for(int b = 0; b < c; b++){
                grids[i][j][k][a] += final[a][b];
            }
        }
    }
    
    int t = 1;
    
    while(T--){
        cin >> r >> c >> m;
        cout << "Case #" << t++ << ":" << endl;
        if(ans[r][c][m]){
            assert(grids[r][c][m].size() == r);
            for(int i = 0; i < r; i++){
                cout << grids[r][c][m][i] << endl;
            }
        }else{
            cout << "Impossible" << endl;
        }
    }
    
    
    return 0;
}