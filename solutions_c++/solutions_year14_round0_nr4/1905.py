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
    	int n;
        cin >> n;
        vector<double> alice(n), bob(n);
        for (int i = 0; i< n; ++i)
            cin >> alice[i];
        for (int i = 0; i< n; ++i)
            cin >> bob[i];
        sort(alice.begin(), alice.end());
        sort(bob.begin(), bob.end());

        int y = 0;
        int ia = 0, ib = 0;
        while (ia < n && ib < n) {
            while (ia < n && alice[ia] < bob[ib])
                ++ia;
            if (ia < n) {
                y++;
                ia++;
                ib++;
            }
        }
        
        vector<pair<double, int> > ab;
        for (int i = 0; i < n; ++i) {
            ab.push_back(make_pair(alice[i], -1));
        }
        for (int i = 0; i < n; ++i) {
            ab.push_back(make_pair(bob[i], 1));
        }
        sort(ab.begin(), ab.end());
        int z = 0;
        int cur = 0;
        for (int i = 0; i < ab.size(); ++i) {
            cur += ab[i].second;
            z = max(z, cur);
        }

        cout << "Case #" << testNumber << ": " << y << " " << z << endl;
    }

    return 0;
}
