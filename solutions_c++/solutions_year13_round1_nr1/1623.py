#include <cstdlib>
#include <climits>
#include <cstdio>
#include <cstring>
#include <cmath>

// STL
#include <sstream>
#include <string>
#include <iostream>
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

ll R, T;

ll solve() {
    ll count = 0;
    ll tmp = 2*R + 1;
    while (T >= tmp) {
        ++count;
        R += 2;
        T -= tmp;
        tmp = 2*R + 1;
    }

    return count;
}


int main() {
    ll numcase;

    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small.out", "w", stdout);
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);

    cin >> numcase;
    for (ll i = 0; i < numcase; ++i) {
        cin >> R >> T;
        cout << "Case #" << i + 1 << ": " << solve() << endl;
    }

    return 0;
}
