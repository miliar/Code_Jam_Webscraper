#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cassert>
#include <ctime>
#include <deque>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i ++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i --)
#define mp make_pair
#define pb push_back
#define fs first
#define sc second
#define pi 3.1415926535897932384626433832795l

typedef long long ll;
typedef long double ld;

int n, m;
char c[60][60];
int all;
bool use[60][60];


inline int dfs(int i, int j){
    int kol = 1;
    use[i][j] = true;
    bool q = true;
    for (int dx = -1; dx < 2; dx ++){
        for (int dy = -1; dy < 2; dy ++){
            if (i + dx < 0 || i + dx >= n || j + dy < 0 || j + dy >= m) continue;
            if (c[i + dx][j + dy] == '*'){
                q = false;
                break;
            }
        }
    }
    if (q){
        for (int dx = -1; dx < 2; dx ++){
            for (int dy = -1; dy < 2; dy ++){
                if (i + dx < 0 || i + dx >= n || j + dy < 0 || j + dy >= m || use[i + dx][j + dy]) continue;
                kol += dfs(i + dx, j + dy);
            }
        }    
    }
    return kol;
}

bool check(){
    memset(use, false, sizeof(use));
    forn(i, n){
        forn(j, m){
            if (c[i][j] == '.'){
                bool q = true;
                for (int dx = -1; dx < 2; dx ++){
                    for (int dy = -1; dy < 2; dy ++){
                        if (i + dx < 0 || i + dx >= n || j + dy < 0 || j + dy >= m) continue;
                        if (c[i + dx][j + dy] == '*'){
                            q = false;
                            break;
                        }
                    } 
                }
                if (q || all == 1){
                    if (dfs(i, j) == all){
                        c[i][j] = 'c';
                        return true;
                    }
                }
            } 
        }
    }
    return false;
}

bool calc(int i, int j, int kol){
    //cerr << i << ' ' << j << ' ' << kol << endl;
    if (kol < 0) return false;
    if (i == n && j == 0){
        if (kol != 0) return false;
        if (check()){
            return true;
        } else
            return false;
    }
    c[i][j] = '.';
    int nexti = i, nextj = j + 1;
    if (j == m - 1){
        nexti ++;
        nextj = 0;
    }
    if (calc(nexti, nextj, kol - 1))
        return true;
    c[i][j] = '*';
    if (calc(nexti, nextj, kol))
        return true;
    return false;
}

int main(){
#ifdef SG
    freopen ("input.txt","rt",stdin);
  freopen ("output.txt","wt",stdout);
#endif  
    int t;
    cin >> t;
    forn(qqq, t){   
        cerr << qqq + 1 << endl;
        cin >> n >> m >> all;
        cout << "Case #" << qqq + 1 << ":" << endl;
        all = n * m - all;
        if (calc(0, 0, all)){
            forn(i, n){
                forn(j, m){
                    cout << c[i][j];
                }
                cout << endl;
            }
        } else {
            cout << "Impossible" << endl;
        }
    }



    return 0;
}
