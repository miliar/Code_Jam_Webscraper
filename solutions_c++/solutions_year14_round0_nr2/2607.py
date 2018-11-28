#include <cstdlib>
#include <climits>
#include <cstdio>
#include <cstring>
#include <cmath>

// STL
#include <sstream>
#include <string>
#include <iostream>
#include <iomanip>
#include <limits>
#include <algorithm>
#include <vector>
#include <map> // contains multimap
#include <set> // contains multiset
#include <queue> // contains priority_queue
#include <deque>
#include <list>
#include <stack>

using namespace std;

typedef unsigned long long ul;
typedef long long ll;

#define SIZE 1000

double C, F, X;

double solve() {
    double best = 1e15, cur = 1e15-1;
    double cps = 2, time = 0;
    while (cur < best) {
        best = cur;
        cur = time + X / cps;
        time += C / cps;
        cps += F;
        //cout << endl << cur << endl;
    }
    return best;
}


int main() {
    int numcase;

    //freopen("B-small-attempt0.in", "r", stdin);
    //freopen("B-small.out", "w", stdout);
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    cin >> numcase;
    for (int i = 0; i < numcase; ++i) {
        cin >> C >> F >> X;
        cout << "Case #" << i + 1 << ": ";
        cout << setprecision(7) << fixed;
        cout << solve() << endl;
    }

    return 0;
}
