
/**
 * author : dpsipher
 */
#include <cstdio>
#include <numeric>
#include <iostream>
#include <vector>
#include <set>
#include <cstring>
#include <string>
#include <map>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <bitset>
#include <queue>
#include <sstream>
#include <deque>
#include <cassert>

using namespace std;

#define mp make_pair
#define pb push_back
#define rep(i,n) for(int i = 0; i < (n); i++)
#define re return
#define fi first
#define se second
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define fill(x,y) memset(x,y,sizeof(x))
#define FOREACH(it,v)   for(typeof((v).begin()) it=(v).begin();it != (v).end();it++)
#define i(x) scanf("%d",&x)
#define u(x) scanf("%u",&x)
#define l(x) scanf("%l64d",&x)
#define ul(x) scanf("%l64u",&x)

typedef long long ll;
typedef unsigned int ui;
typedef unsigned long long ull;
typedef long double ld;                         
typedef vector<int> vi;

typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<vi> vvi;

using namespace std;
int r, c;
char grid[101][101];
int cycle[101][101];
bool vis[101][101];
int dfs(int i, int j)
{
    if (i >= r || i < 0 || j >= c || j < 0) return 0;
    if (vis[i][j]){ cycle[i][j] = 1; return 1;}
    vis[i][j] = true;
    if (grid[i][j] == '>') {
        cycle[i][j] = dfs(i,j+1);
    } else if (grid[i][j] == '<') {
        cycle[i][j] = dfs(i,j-1);
    } else if (grid[i][j] == '^') {
        cycle[i][j] = dfs(i-1,j);
    } else if (grid[i][j] == 'v') {
        cycle[i][j] = dfs(i+1,j);
    }
    return cycle[i][j];
}

int endPoint(int i, int j, char dir)
{
    if (i >= r || i < 0 || j >= c || j < 0) return -1;
    
    if (vis[i][j]) {return 1;}
    vis[i][j] = true;
    if (grid[i][j] != '.') return 1;
    else if (dir == '>') {
        return endPoint(i,j+1, dir);
    } else if (dir == '<') {
        return endPoint(i,j-1, dir);
    } else if (dir == '^') {
        return endPoint(i-1,j, dir);
    } else if (dir == 'v'){
        return endPoint(i+1,j, dir);
    } 
}
int main()
{
    int tests;
    i(tests);
    string dir = "><^v";
    rep(testno, tests) {
        printf("Case #%d: ", testno+1);
        memset(grid, 0 ,sizeof grid);
        memset(cycle, 0 ,sizeof cycle);
        memset(vis, 0 ,sizeof vis);
        cin >> r >> c;
        string str;
        rep(i,r) {cin >> str;rep(j,c) grid[i][j] = str[j];}
        
        rep(i,r) {rep(j,c){memset(vis, 0 ,sizeof vis); dfs(i,j); /*cout << cycle[i][j];*/}/*cout << endl;*/}
        int res = 0;
        bool imp = false;
        rep(i,r) {rep(j,c) {
                if (grid[i][j] != '.' && cycle[i][j] == 0) {
                    memset(vis, 0, sizeof vis);
                    char c = grid[i][j];
                    grid[i][j] = '.';
                    if (endPoint(i,j, c) == -1) { // if edge
                        grid[i][j] = c;
                        bool f = 0;
                        for (int k = 0; k < 4; k++) {
                            char c = grid[i][j];
                            grid[i][j] = '.';
                            memset(vis, 0, sizeof vis);
                            if (endPoint(i,j, dir[k]) != -1) {
                                grid[i][j] = c;
                                f = 1;
                                break;
                            }
                            grid[i][j] = c;
                        }
                        
                        if (f) {
                            res++;
                        } else {
                            imp = true;
                            break;
                        }
                    }
                    grid[i][j] = c;
                }
            } 
            if (imp) break;
        }
        if (imp) cout << "IMPOSSIBLE\n";
        else cout << res << endl;

    }
    return 0;
}
