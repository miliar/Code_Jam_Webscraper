
#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <complex>
#include <algorithm>
#include <numeric>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cassert>
//STL Debug Mode
#define _GLIBCXX_DEBUG 
#define REP(i,n) for(int i=0;i<(int)n;i++)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();i++)
#define ALL(c) (c).begin(),(c).end()
#define PB push_back
#define MP make_pair
using namespace std;
typedef pair<int,int> PII;
typedef long long ll;
const int INFI = (1<<28);
const ll INFL = (1LL<<60);
const double INFD = (1e+300);
const double EPS = (1e-8);
//int dx[] = {1,-1,0,0};
//int dy[] = {0,0,1,-1};
//struct P { int cost; bool operator < (const P &p) const { return cost > p.cost; } };

int main(){
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int n;
    cin >> n;
    for (int c = 1; c <= n; c++) {
        string f[4];
        bool end = true;
        cin >> f[0] >> f[1] >> f[2] >> f[3];
        int x,o;
        bool wx = false, wo = false;
        for (int i = 0; i < 4; i++) {
            x = o = 0;
            for (int j = 0; j < 4; j++) {
                if (f[i][j] == '.') end = false;
                if (f[i][j] == 'X' || f[i][j] == 'T') x++;
                if (f[i][j] == 'O' || f[i][j] == 'T') o++;
            }
            if (x == 4) wx = true;
            if (o == 4) wo = true;
        }
        for (int i = 0; i < 4; i++) {
            x = o = 0;
            for (int j = 0; j < 4; j++) {
                if (f[j][i] == 'X' || f[j][i] == 'T') x++;
                if (f[j][i] == 'O' || f[j][i] == 'T') o++;
            }
            if (x == 4) wx = true;
            if (o == 4) wo = true;
        }
        x = o = 0;
        for (int i = 0; i < 4; i++) {
            if (f[i][i] == 'X' || f[i][i] == 'T') x++;
            if (f[i][i] == 'O' || f[i][i] == 'T') o++;
        }
        if (x == 4) wx = true;
        if (o == 4) wo = true;
        x = o = 0;
        for (int i = 0; i < 4; i++) {
            if (f[3-i][i] == 'X' || f[3-i][i] == 'T') x++;
            if (f[3-i][i] == 'O' || f[3-i][i] == 'T') o++;
        }
        if (x == 4) wx = true;
        if (o == 4) wo = true;

        cout << "Case #" << c << ": ";
        if (wx) cout << "X won";
        else if (wo) cout << "O won";
        else if (end) cout << "Draw";
        else cout << "Game has not completed";
        cout << endl;
    }

    return 0;
}
