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
const int ssize = 15;

map <pair <int, int>, string> level[ssize][3];

int winner(int a, int b) {
    if (a == b) {
        assert(false);
    }
    if (a + b == 1)
        return 0;
    if (a + b == 2)
        return 2;
    return 1;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    level[0][0][mp(1, 0)] = "P";
    level[0][1][mp(0, 1)] = "R";
    level[0][2][mp(0, 0)] = "S";

    for (int i = 1; i < ssize; i++) {
        for (int j = 0; j < 3; j++)
            for (int k = 0; k < 3; k++) {
                if (j != k) {
                    for (auto& e1 : level[i - 1][j])
                        for (auto& e2 : level[i - 1][k]) {
                            string res = level[i][winner(j, k)][mp(e1.fs.fs + e2.fs.fs, e1.fs.sc + e2.fs.sc)];
                            if (res == "")
                                res = "Z";
                            res = min(res, e1.sc + e2.sc); 
                            level[i][winner(j, k)][mp(e1.fs.fs + e2.fs.fs, e1.fs.sc + e2.fs.sc)] = res;                             
                        }
                }
            }
    
        for (int j = 0; j < 3; j++)
            cerr << level[i][j].size() << endl;
    } 
   
//    return 0;


    int tc;

    cin >> tc;
    for (int tnum = 0; tnum < tc; tnum++) {
        int n, r, p, s;
        cin >> n >> r >> p >> s;

        string res = "Z";
        for (int i = 0; i < 3; i++)
            if (level[n][i].find(mp(p, r)) != level[n][i].end())
                res = min(res, level[n][i][mp(p, r)]);

        if (res == "Z")
            cout << "Case #" << tnum + 1 << ": IMPOSSIBLE" << endl;
        else
            cout << "Case #" << tnum + 1 << ": " << res << endl;
         
    }

    return 0;
}