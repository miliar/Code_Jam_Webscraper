#include <bits/stdc++.h>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define mms(v) memset(v,0,sizeof(v))
using namespace std;

pair<bool, char> simulate(string s){
    string l, r;
    int metade = s.size() / 2;
    l = s.substr(0, metade);
    r = s.substr(metade, metade);
    int tam = l.size();
    if (tam == 1 && l == r) return mp(false, ' ');
    else if (tam == 1){
        if (l == "R" && r == "S" || l == "S" && r == "R") return mp(true, 'R');
        else if (l == "S" && r == "P" || l == "P" && r == "S") return mp(true, 'S');
        else return mp(true, 'P');
    }
    pair<bool, char> ret1, ret2;
    ret1 = simulate(l);
    ret2 = simulate(r);

    if (!ret1.fi || !ret2.fi) return mp(false, ' ');

    if (ret1.se == ret2.se) return mp(false, ' ');

    if (ret1.se == 'R' && ret2.se == 'S' || ret1.se == 'S' && ret2.se == 'R') return mp(true, 'R');
    else if (ret1.se == 'S' && ret2.se == 'P' || ret1.se == 'P' && ret2.se == 'S') return mp(true, 'S');
    else return mp(true, 'P');
}
int main(){
    int t;
    cin >> t;

    for (int i = 0; i < t; i++){
        cout << "Case #" << i + 1 << ": ";
        int n, r, p, s;
        vector<string> v;
        cin >> n >> r >> p >> s;
        string res;
        for (int i = 0; i < p; i++){
            res += 'P';
        }
        for (int i = 0; i < r; i++){
            res += 'R';
        }
        for (int i = 0; i < s; i++){
            res += 'S';
        }
        char c = ' ';
        bool good = false;
        do{
            if (simulate(res).first){
                cout << res << endl;
                good = true;
                break;
               }
        }while (next_permutation(res.begin(), res.end()));
        if (!good) cout << "IMPOSSIBLE" << endl;
    }

}
