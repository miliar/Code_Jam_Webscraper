#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

const int N = 107;

int n, m, a[N][N];
int pr[N], p[N];
string s[N];

void solve(){
    int x, y;
    cin >> n >> m;
    int id = -1;
    for (int i = 0; i < n; i++) {
        cin >> s[i];
        if (id == -1 || s[i] < s[id]) id = i;
    }
    p[0] = id;
    for (int i = 1; i < n; i++){
        if (i <= id) p[i] = i-1;
        else p[i] = i;
    }
    memset(a,0,sizeof(a));
    for (int i = 0; i < m; i++) {
        cin >> x >> y;x--, y--;
        a[x][y] = a[y][x] = 1;
    }
    int v = id; 
    string res = "z";
    string cur;
    bool ok;
    
    do{
        if (p[0] != id) break;
        v = id;
        pr[v] = -1;
        ok = 1;
        cur = s[id];
        for (int i = 1; i < n; i++) {
            while (v >= 0 && !a[v][p[i]]) v = pr[v];
            if (v == -1) {ok = 0;break;}
            pr[p[i]] = v;
            v = p[i];
            cur += s[v];
        }
        if (ok) res = min(res, cur);
    }while(next_permutation(p,p+n));
    cout << res << endl;
}

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++){
        cout << "Case #" << i+1 << ": ";
        solve();
    }
    return 0;
}
