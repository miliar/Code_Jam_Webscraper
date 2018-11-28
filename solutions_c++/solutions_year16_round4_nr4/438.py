#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

#define pb push_back
#define mp make_pair
#define fs first
#define sc second

const double pi = acos(-1.0);
const int size = 100;
const int inf = 1000 * 1000;

bool best;
bool flag;
int n;
int used[2][size];
bool way[size][size];

void dfs(int side, int v, int cl) {
    used[side][v] = cl;

    if (side == 0) {
        for (int i = 0; i < n; i++)
            if (way[v][i] && used[1][i] == -1)
                dfs(1, i, cl);
    } else {
        for (int i = 0; i < n; i++)
            if (way[i][v] && used[0][i] == -1)
                dfs(0, i, cl);
    }         
}

/*
bool connected(int n) {
    for (int i = 0; i < n; i++)
        used[0][i] = used[1][i] = false;
    dfs(0, 0);

    bool flag = true;
    for (int i = 0; i < n; i++)
        flag = flag && used[0][i] && used[1][i];

    return flag;
}

void rec(int p, int n) {
    if (flag)
        return;
    if (p == n) {
        bool check = true;
        int cnt = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (!used[0][i] && !used[1][j]) {
                    check = check && !way[i][j];
                    cnt++;
                }

        if (cnt == 0)
            best = true;
        flag = flag || (cnt > 0 && check);

        return; 
    }

    rec(p + 1, n);
    for (int i = 0; i < n; i++)
        if (way[p][i] && !used[1][i]) {
            used[0][p] = true;
            used[1][i] = true;

            rec(p + 1, n);

            used[0][p] = used[1][i] = false;
        }
}
*/

vector <pair <int, int> > comps;

int rans = 0;
int a, b;
int curb[size];
int curs[size];
int cur;
int tc;
char field[size][size];

void rec(int p, int lim) {
    if (p == lim) {
        int na = 0;
        int nb = 0;
        int cans = 0;

//        cerr << "found" << endl;
        /*
        for (int i = 0; i < cur; i++) {
  //          cerr << curb[i] << ' ' << curs[i] << endl;
            if (curb[i] < 0) {
                nb += -curb[i];
                cans += curs[i] * curs[i];
            }
            if (curb[i] > 0) {
                na += curb[i];
                cans += (curs[i] + curb[i]) * (curs[i] + curb[i]);
            }
        }
        if (nb > b || na > a)
            return;
        */
        //rans = min(rans, cans + (b - nb));
        
        for (int i = 0; i < cur; i++)
            if (curb[i] != 0) {
                return;
            } else {
                cans += curs[i] * curs[i];
            }
        rans = min(rans, cans);

        return; 
    }

    curb[cur] = comps[p].fs;
    curs[cur] = comps[p].sc;
    cur++;
    rec(p + 1, lim);
    cur--;
    curb[cur] = 0;
    curs[cur] = 0;

    for (int i = 0; i < cur; i++) {
        if (curb[i] == 0)
            continue;
        curb[i] += comps[p].fs;
        curs[i] += comps[p].sc;
        rec(p + 1, lim);
        curb[i] -= comps[p].fs;
        curs[i] -= comps[p].sc;
    }
}

int solve() {
    int ans = 0;
    a = 0;
    b = 0;

    /*
    vector <pair <int, int> > ncomps;
    for (int i = 0; i < (int) comps.size(); i++) {
        if (comps[i].fs == 0) {
            ans += comps[i].sc * comps[i].sc; 
            continue;
        }
        if (comps[i].fs == 1 && comps[i].sc == 0) {
            b++;
            continue;        
        }
        if (comps[i].fs == -1 && comps[i].sc == 1) {
            a++;
            continue;
        }
        ncomps.pb(comps[i]);
    }
    */

    //comps = ncomps;    
    sort(comps.begin(), comps.end());

    cur = 0;
    rans = inf;
    rec(0, (int) comps.size());

    return rans + ans;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> tc;
    for (int tnum = 0; tnum < tc; tnum++) {
        comps.clear();
        cin >> n;
        for (int i = 0; i < n; i++)
            cin >> field[i];

        int cnt = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) {
                way[i][j] = (field[i][j] == '1');
                cnt += way[i][j];
            }

        for (int i = 0; i < n; i++)
            used[0][i] = used[1][i] = -1;

        int tot = 0;
        for (int i = 0; i < 2; i++)
            for (int j = 0; j < n; j++)
                if (used[i][j] == -1)
                    dfs(i, j, tot++);


        for (int i = 0; i < tot; i++) {
            int a = 0;
            int b = 0;
            for (int j = 0; j < n; j++) {
                a += (used[0][j] == i);
                b += (used[1][j] == i);
            }

            comps.pb(mp(b - a, a));
        }

        printf("Case #%d: %d\n", tnum + 1, solve() - cnt);
    }

    /*
    cin >> n;

    for (int msk = 0; msk < (1 << (n * n)); msk++) {
        for (int j = 0; j < n; j++)
            for (int k = 0; k < n; k++) {
                way[j][k] = (msk >> (j * n + k)) & 1;
            }

        if (!connected(n)) {
            continue;
        }

        best = false;
        flag = false;
        for (int i = 0; i < n; i++)
            used[0][i] = used[1][i] = false;
        rec(0, n);
//        cerr << msk << ' ' << flag << endl;
        if (best && !flag) {
            cout << msk << endl;
        }
    }
    */

    return 0;
}