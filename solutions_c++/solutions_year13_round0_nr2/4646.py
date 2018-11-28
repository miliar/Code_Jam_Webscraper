//In the name of Allah
#include <iostream>
using namespace std;

#define FOR(i, n) for(int i = 0; i < (n); i++)
#define FORB(i, a, b) for(int i = (a); i <= (b); i++)
const int N = 100 +2;
int a[N][N];
int b[N][N];
int n, m;

bool cut[2][N];

bool good(){
    memset(cut, 0, sizeof(cut));

    FOR(i, n)FOR(j, m){
        if (b[i][j] == 0 || cut[0][i] || cut[1][j]) continue;
        //cerr << " i : " << i << " j: " << j << "  " << cut[0][i] << " " << cut[1][j] << endl;
        //if (i && j) {cerr <<"------\n"; return false;}

        bool canCutRow = true, canCutCol = true;

        FOR(k, m)   if (b[i][k] == 0)   canCutRow = false;
        if (canCutRow)  cut[0][i] = 1;


        FOR(k, n)   if (b[k][j] == 0)   canCutCol = false;
        if (canCutCol) cut[1][j] = 1;

        if (canCutRow == false && canCutCol == false){
          //  cerr <<"XXXX\n";
            return false;
        }
    }
    return true;
}

string solve(){
    FORB(k, 1, 100){
        FOR(i, n)FOR(j, m)
            b[i][j] = (a[i][j] <= k);
        if (!good())
            return "NO";
    }
    return "YES";
}

int main(){
    int tests;
    cin >> tests;
    for (int tt = 1; tt <= tests; tt++){
        cin >> n >> m;
        FOR(i, n)FOR(j, m)  cin >> a[i][j];
        cout << "Case #" << tt << ": " << solve() << endl;
    }
    return 0;
}
