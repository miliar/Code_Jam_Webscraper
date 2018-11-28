// vudduu - codejam 2016 Round 2
// Problem A
#include <iostream>
#include <sstream>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <functional>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <stdio.h>
#include <string.h>
using namespace std;

#define FOR(i,a,b)  for(int i=(a),_##i=(b);i<_##i;++i)
#define F(i,a)      FOR(i,0,a)
#define ALL(x)      x.begin(),x.end()
#define PB          push_back
#define MP          make_pair
#define S           size()
typedef long long   LL;

const string str("RPS");
int rps[3];
bool good;
int N;

string createTree(int winner, int x, int y) {
    string a, b;
    if(x == y) {
        string res(".");
        res[0] = str[winner];
        return res;
    }
    int mid = (x+y) >> 1;
    if(winner == 0) {
        if(rps[2] > 0) {
            rps[2]--;
            a = createTree(0, x, mid); // R
            b = createTree(2, mid+1, y); // S
        }
        else good = false;
    }
    if(winner == 1) {
        if(rps[0] > 0) {
            rps[0]--;
            a = createTree(1, x, mid); // P
            b = createTree(0, mid+1, y); // R
        }
        else good = false;
    }
    if(winner == 2) {
        if(rps[1] > 0) {
            rps[1]--;
            a = createTree(1, x, mid); // P
            b = createTree(2, mid+1, y); // S
        }
        else good = false;
    }
    if(!good) return "";
    if(a < b) {
        F(i, b.S) a.PB(b[i]);
        return a;
    }
    else {
        F(i, a.S) b.PB(a[i]);
        return b;
    }
}

void solve() {
    cin >> N >> rps[0] >> rps[1] >> rps[2];
    N = 1 << N;
    string res;
    F(i, 3) {
        int bac0 = rps[0];
        int bac1 = rps[1];
        int bac2 = rps[2];
        if(rps[i] > 0) {
            rps[i]--;
            good = true;
            string solu = createTree(i, 0, N-1);
            if(good) {
                if(res.S == 0 || res > solu)
                    res = solu;
            }
        }
        rps[0] = bac0;
        rps[1] = bac1;
        rps[2] = bac2;
    }
    if(res.S)
        cout << res << endl;
    else
        cout << "IMPOSSIBLE" << endl;
}

int main() {
	// freopen("in.txt", "r", stdin);
	// freopen("A-small-attempt2.in", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
    scanf("%d", &T);
    for(int cas=1; cas<=T ;cas++) {
        printf("Case #%d: ", cas);
        solve();
    }
}
