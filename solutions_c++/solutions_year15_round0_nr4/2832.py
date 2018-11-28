#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <map>
#include <set>
#include <list>
#include <vector>
#include <stack>
#include <queue>
#include <bitset>
#include <iterator>
#include <cstring>
#include <climits>
#include <cmath>
#include <cassert>

using namespace std;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for (int i=0; i<(n); ++i)
#define FOR(var,start,end) for (int var=(start); var<=(end); ++var)
#define FORD(var,start,end) for (int var=(start); var>=(end); --var)
#define FOREACH(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define SIZE(x) ((int)((x).size()))

// typedef long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector< vector<int> > VVI;
typedef vector< vector<bool> > VVB;

typedef bool (*F)(int, int);

static bool x1(int r, int c) {
    return true;
}

static bool x2(int r, int c) {
    if (r == 1 && c == 1) {
        return false;
    }
    if ((r == 1 && c == 2) || (r == 2 && c == 1)) {
        return true;
    }
    if ((r == 1 && c == 3) || (r == 3 && c == 1)) {
        return false;
    }
    if ((r == 1 && c == 4) || (r == 4 && c == 1)) {
        return true;
    }
    if (r == 2 && c == 2) {
        return true;
    }
    if ((r == 2 && c == 3) || (r == 3 && c == 2)) {
        return true;
    }
    if ((r == 2 && c == 4) || (r == 4 && c == 2)) {
        return true;
    }
    if (r == 3 && c == 3) {
        return false;
    }
    if ((r == 3 && c == 4) || (r == 4 && c == 3)) {
        return true;
    }
    if (r == 4 && c == 4) {
        return true;
    }
    assert(false);
    return false;
}

static bool x3(int r, int c) {
    if (r == 1 && c == 1) {
        return false;
    }
    if ((r == 1 && c == 2) || (r == 2 && c == 1)) {
        return false;
    }
    if ((r == 1 && c == 3) || (r == 3 && c == 1)) {
        return false;
    }
    if ((r == 1 && c == 4) || (r == 4 && c == 1)) {
        return false;
    }
    if (r == 2 && c == 2) {
        return false;
    }
    if ((r == 2 && c == 3) || (r == 3 && c == 2)) {
        return true;
    }
    if ((r == 2 && c == 4) || (r == 4 && c == 2)) {
        return false;
    }
    if (r == 3 && c == 3) {
        return true;
    }
    if ((r == 3 && c == 4) || (r == 4 && c == 3)) {
        return true;
    }
    if (r == 4 && c == 4) {
        return false;
    }
    assert(false);
    return false;
}

static bool x4(int r, int c) {
    if (r == 1 && c == 1) {
        return false;
    }
    if ((r == 1 && c == 2) || (r == 2 && c == 1)) {
        return false;
    }
    if ((r == 1 && c == 3) || (r == 3 && c == 1)) {
        return false;
    }
    if ((r == 1 && c == 4) || (r == 4 && c == 1)) {
        return false;
    }
    if (r == 2 && c == 2) {
        return false;
    }
    if ((r == 2 && c == 3) || (r == 3 && c == 2)) {
        return false;
    }
    if ((r == 2 && c == 4) || (r == 4 && c == 2)) {
        return false;
    }
    if (r == 3 && c == 3) {
        return false;
    }
    if ((r == 3 && c == 4) || (r == 4 && c == 3)) {
        return true;
    }
    if (r == 4 && c == 4) {
        return true;
    }
    assert(false);
    return false;
}

static F fs[5] = { NULL, x1, x2, x3, x4 };

static bool go(int x, int r, int c) {
    return fs[x](r, c);
}

int main() {
    int nTests = 0; cin >> nTests;
    FOR (test, 1, nTests) {
        int x = 0; int r = 0; int c = 0;
        cin >> x >> r >> c;
        cout << "Case #" << test << ": ";
        cout << (go(x, r, c) ? "GABRIEL" : "RICHARD") << "\n";
    }

    return 0;
}

