#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
#include <memory.h>
#include <string>
#include <sstream>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;

#define MP make_pair
#define PB push_back
#define FF first
#define SS second

#define FORN(i, n) for (int i = 0; i <  (int)(n); i++)
#define FOR1(i, n) for (int i = 1; i <= (int)(n); i++)
#define FORD(i, n) for (int i = (int)(n) - 1; i >= 0; i--)

#define DEBUG(X) { cout << #X << " = " << (X) << endl; }
#define PR0(A,n) { cout << #A << " = "; FORN(_,n) cout << A[_] << ' '; cout << endl; }

#define MOD 1000000007
#define INF 2000000000

int GLL(LL& x) {
    return scanf("%lld", &x);
}

int GI(int& x) {
    return scanf("%d", &x);
}

int T;

string state; int k;

void flip(char& c) {
    if (c == '+') {
        c = '-';
    }
    else {
        c = '+';
    }
}

void solve() {
    int n = state.size();

    int i = 0; int res = 0;

    while (i < n) {
        if (state[i] == '-') {
            if (i + k - 1 < n) {
                for (int j = i; j < i + k; j++) {
                    flip(state[j]);
                }
                res++;
            }
            else {
                printf("IMPOSSIBLE\n");
                return;
            }
        }
        i++;
    }
    printf("%d\n", res);
}

int main() {
    GI(T);

    FOR1(t, T) {
        printf("Case #%d: ", t);

        cin >> state;
        GI(k);

        solve();
    }

    return 0;
}
