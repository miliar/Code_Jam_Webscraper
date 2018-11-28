#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <bitset>
#include <set>
#include <sstream>
#include <stdlib.h>
#include <map>
#include <queue>
#include <stack>
#include <assert.h>

using namespace std;

#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

#define forit(X,Y) for(typeof((Y).begin()) X = (Y).begin(); X != (Y).end(); ++X)

#define debug(x) cout << '>' << #x << ':' << x << endl;

typedef long long int64;

typedef vector <int> vi;
typedef vector < vi > vvi;


const double INF = 1000000;
const double EPS = 1E-6;

typedef pair<pair<int, int>, pair<int, int> > Rect;

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

	int testCount;
    cin >> testCount;

    for (int testNumber = 1; testNumber <= testCount; ++testNumber) {
    	double C, F, X;
        cin >> C >> F >> X;

        double income = 2.0;
        double best = X / income;
        double last_cookie = 0.0;
        while (best > last_cookie) {
            last_cookie += C / income;
            income += F;
            double res = last_cookie + X / income;
            if (res < best)
                best = res;
        }
        std::cout.setf( std::ios::fixed, std:: ios::floatfield );
        cout.precision(7);
        cout << "Case #" << testNumber << ": " << best << endl;
    }

    return 0;
}
