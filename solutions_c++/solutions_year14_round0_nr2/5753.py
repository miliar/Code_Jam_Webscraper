#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <utility>
#include <iomanip>
#include <climits>

#define PB push_back
#define MP make_pair
#define MAX 1e10
#define EPS 1e-9
#define all(v) v.begin(),v.end()

using namespace std;

int nTest, cases;
double C, F, X;

int gcd(int a, int b){return (a * b ? gcd(min(a, b), max(a, b) % min(a, b)) : max(a, b));}

double solve(double f) {
    if(f > 10.0 * X) return X / f;
    return min(X / f, C / f + solve(f + F));
}

int main() {
	freopen("B-small-attempt2.in", "r", stdin);
	freopen("B-small-attempt2.out", "w", stdout);

    cin >> nTest;

    while(nTest--) {
        cin >> C >> F >> X;
        cout << "Case #" << ++cases << ": " << fixed << setprecision(8) << solve(2.0) << endl;
    }

	return 0;
}
