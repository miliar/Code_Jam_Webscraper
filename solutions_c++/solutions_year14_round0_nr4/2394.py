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

int N;
double naomi[SIZE];
double ken[SIZE];

int war() {
    int score = 0;
    double* kn = ken;
    for (int i = 0; i < N; ++i) {
        if (*kn > naomi[i]) ++kn;
        else ++score;
    }
    return score;
}

int deceitful() {
    int score = 0;
    double* nm = naomi;
    for (int i = 0; i < N; ++i) {
        if (*nm > ken[i]) {++nm; ++score;}
    }
    return score;
}

int solve() {
    sort(naomi,naomi+N, greater<double>());
    sort(ken,ken+N, greater<double>());

    cout << deceitful() << " " << war();
    return 0;
}


int main() {
    int numcase;

    //freopen("D-small-attempt0.in", "r", stdin);
    //freopen("D-small.out", "w", stdout);
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);

    cin >> numcase;
    for (int i = 0; i < numcase; ++i) {
        cin >> N;
        memset(naomi, 0, sizeof(double)*N);
        memset(ken, 0, sizeof(double)*N);
        for  (int j = 0; j < N; ++j) {
            cin >> naomi[j];
        }
        for  (int j = 0; j < N; ++j) {
            cin >> ken[j];
        }
        cout << "Case #" << i + 1 << ": ";
        solve();
        cout << endl;
    }

    return 0;
}
