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

#define SIZE 4

int input1[SIZE];

int solve() {
    return 0;
}


int main() {
    int numcase, n, n2, res, count;

    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small.out", "w", stdout);
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);

    cin >> numcase;
    for (int i = 0; i < numcase; ++i) {
        res = -1;
        count = 0;

        cin >> n;
        for (int k = 1; k <= SIZE; ++k) {
            if (k!=n) {
                cin >> n2 >> n2 >> n2 >> n2;
                continue;
            }
            for (int l = 0; l < SIZE; ++l) {
                cin >> input1[l];
            }
        }

        cin >> n;
        for (int k = 1; k <= SIZE; ++k) {
            if (k!=n) {
                cin >> n2 >> n2 >> n2 >> n2;
                continue;
            }
            for (int l = 0; l < SIZE; ++l) {
                cin >> n2;
                for (int f = 0; f<SIZE; ++f) {
                    if (n2 != input1[f]) continue;
                    res = n2; ++count;
                }
            }
        }
        cout << "Case #" << i + 1 << ": ";
        if (count > 1) cout << "Bad magician!";
        else if (count == 0) cout << "Volunteer cheated!";
        else cout << res;
        cout << endl;
    }

    return 0;
}
