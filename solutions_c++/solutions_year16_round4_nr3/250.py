#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <algorithm>

#define fii(x,y) for(int i=x;i<y;i++)
#define fjj(x,y) for(int j=x;j<y;j++)
#define fkk(x,y) for(int k=x;k<y;k++)
#define fi(x) fii(0,x)
#define fj(x) fjj(0,x)
#define fk(x) fkk(0,x)
#define eps 0.0000000001
#define inf 1<<28

using namespace std;

typedef long long ll;
typedef vector <int> VI;
typedef vector <VI> VVI;
typedef vector <VVI> VVVI;
typedef vector <ll> VL;
typedef vector <VL> VVL;
typedef vector <double> VD;
typedef vector <VD> VVD;
typedef vector <bool> VB;
typedef vector <VB> VVB;
typedef queue <int> QI;
typedef pair<int,int> PI;
typedef pair<int,PI> PT;
typedef queue<PI> QPI;
typedef priority_queue<PT> QPT;
typedef pair<double,double> PD;

string itc = "/\\";

bool sigue (int& row, int& col, int& dir, int mp, int r, int c) {
    int nr, nc, nd;
    if (dir == 0) {
        if (mp == 0) {
            nr = row;
            nc = col - 1;
            nd = 1;
        } else {
            nr = row;
            nc = col + 1;
            nd = 3;
        }
    } else if (dir == 1) {
        if (mp == 0) {
            nr = row + 1;
            nc = col;
            nd = 0;
        } else {
            nr = row - 1;
            nc = col;
            nd = 2;
        }
    } else if (dir == 2) {
        if (mp == 0) {
            nr = row;
            nc = col + 1;
            nd = 3;
        } else {
            nr = row;
            nc = col - 1;
            nd = 1;
        }
    } else if (dir == 3) {
        if (mp == 0) {
            nr = row - 1;
            nc = col;
            nd = 2;
        } else {
            nr = row + 1;
            nc = col;
            nd = 0;
        }
    }
    row = nr;
    col = nc;
    dir = nd;
    if (nr < 0 or nr >= r or nc < 0 or nc >= c)
        return false;
    return true;
}

int extrem (vector<vector<int> >& mapa, int ini) {
    int r = mapa.size();
    int c = mapa[0].size();
    int ri, ci, dir;
    if (ini < c) {
        ri = 0;
        ci = ini;
        dir = 0;
    } else if (ini < c + r) {
        ri = ini - c;
        ci = c - 1;
        dir = 1;
    } else if (ini < c + r + c) {
        ri = r - 1;
        ci = c - (ini - c - r) - 1;
        dir = 2;
    } else {
        ri = 2 * (r + c) - ini - 1;
        ci = 0;
        dir = 3;
    }
//     cout << ini << " " << ri << " " << ci << " " << dir << endl;
    while (sigue(ri, ci, dir, mapa[ri][ci], r, c));
//     cout << "despues " <<  ini << " " << ri << " " << ci << " " << dir << endl;
    if (dir == 2)
        return ci;
    if (dir == 3)
        return c + ri;
    if (dir == 0)
        return r + c + (c - 1 - ci);
    return 2 * (r + c) - ri - 1;
    
}

bool ok(vector<vector<int> >& mapa, vector<int> pairs) {
//     cout << "entro" << endl;
    for (int i = 0; i < pairs.size(); i += 2) {
        if (extrem(mapa, pairs[i]) != pairs[i+1]) {
//             cout << extrem(mapa, pairs[i]) << " " << pairs[i] << " " << pairs[i+1] << endl;
            return false;
        } else {
//             cout << extrem(mapa, pairs[i]) << " == " << pairs[i+1] << endl;
        }
    }
    return true;
}

vector<string> compute() {
    int r, c;
    cin >> r >> c;
    vector<int> pairs(2*(r+c));
    for (int i = 0; i < pairs.size(); i++)
        cin >> pairs[i];
    for (int i = 0; i < pairs.size(); i++)
        pairs[i]--;
    
    int sz = r * c;
    vector<vector<int> > sol;
    for (int mask = 0; mask < (1<<sz); mask++) {
        int m2 = mask;
        vector<vector<int> > mapa(r, vector<int>(c));
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                mapa[i][j] = m2 % 2;
                m2 /= 2;
            }
        }
        if (ok(mapa, pairs))
            sol = mapa;
    }
    vector<string> ans(sol.size());
    for (int i = 0; i < sol.size(); i++) {
        for (int j = 0; j < sol[i].size(); j++)
            ans[i] += itc[sol[i][j]];
    }
    return ans;
}

int main() {
    int nc;
    cin >> nc;
    for (int caso = 1; caso <= nc; caso++) {
        vector<string> v = compute();
        cout << "Case #" << caso << ":" << endl;
        if (v.size() > 0) {
            for (int i = 0; i < v.size(); i++)
                cout << v[i] << endl;
        } else {
            cout << "IMPOSSIBLE" << endl;
        }
    }
}