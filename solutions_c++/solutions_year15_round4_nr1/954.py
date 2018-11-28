#include <bits/stdc++.h>
#define REP(i, x) for(int i = 0; i < (x); i++)
#define FOR(i, x, y) for(int i = (x); i < (y); i++)
using namespace std;
typedef long long LL;

char tab[103][103];

int main() {
    ios_base::sync_with_stdio(0);
    int TT; cin >> TT;
    for(int T = 1; T <= TT; T++) {
        int r, c;
        int ans = 0;
        bool pos = 1;
        cin >> r >> c;
        REP(i, r) REP(j, c) cin >> tab[i][j];
        REP(i, r) REP(j, c) if(pos) {
            if(tab[i][j] == '.')
                continue;
            bool w, a, s, d;
            w = a = s = d = false;
            FOR(k, j + 1, c)
                if(tab[i][k] != '.')
                    d = true;
            FOR(k, 0, j)
                if(tab[i][k] != '.')
                    a = true;
            FOR(k, i + 1, r)
                if(tab[k][j] != '.')
                    s = true;
            FOR(k, 0, i)
                if(tab[k][j] != '.')
                    w = true;
                
            if(tab[i][j] == '>' && d)
                continue;
            if(tab[i][j] == '<' && a)
                continue;
            if(tab[i][j] == 'v' && s)
                continue;
            if(tab[i][j] == '^' && w)
                continue;
            ans ++;
//             cout << i << " " << j <<" "<<w<<" "<<a<<" "<<s<<" "<<d<<"\n";
            if(w || a || s || d)
                continue;
            else pos = 0;
        }
        
        cout << "Case #"<<T<<": ";
        if(pos)
            cout << ans << "\n";
        else
            cout << "IMPOSSIBLE\n";
    }
    return 0;
}
