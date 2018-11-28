#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <numeric>
#include <iomanip>
#include <cassert>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for(__typeof__((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define mp make_pair
#define pb push_back
#define DBG(...) { if(1) fprintf(stderr, __VA_ARGS__); }
#define DBGDO(X) { if(1) cerr << "DBGDO: " << (#X) << " = " << (X) << endl; }


int cops(ll size, ll* m, int count) {
    while (count > 0 && size > m[0]) {
        size += m[0];
        m++;
        count--;
    }
    if (count == 0) {
        return 0;
    }
    //if ((size*2 - 1) > m[0]) {
    //    // introduce a new mote and directly eat it
    //    size += size - 1;
    //    return 1 + cops(size, m, count);
    //}
    //// remote the last one
    //return 1 + cops(size, m, count - 1);
    
    int v1 = INT_MAX;
    if (size > 1) {
        v1 = 1 + cops(size*2 - 1, m, count);
    }
    int v2 = 1 + cops(size, m, count - 1);
    // remote the last one
    return (v1 < v2) ? v1 : v2;
}

int main() {
    ll motes[101];
    int N;
    ll A;
    int TC;
    cin >> TC;
    FOR (t, 1, TC+1) {
        cin >> A >> N;
        FOR (i, 0,N) cin >> motes[i];
        sort(motes+0, motes+N);
        int c = cops(A, motes, N);
        printf("Case #%d: %d\n", t, c);
    }
    return 0;
}

