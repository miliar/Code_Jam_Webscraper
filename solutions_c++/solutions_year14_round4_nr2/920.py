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

#define mplus(x, y) ((x) == -1 || (y) == -1) ? -1 : ((x) + (y))
#define mmax(x, y) ((x) == -1 || (y) == -1) ? -1 : max((x), (y))
#define mmin(x, y) ((x) == -1) ? (y) : ((y) == -1) ? (x) : min((x), (y))

#define checkbit(n, k) (((1L << (k)) & (n)) != 0)

#define forit(X,Y) for(typeof((Y).begin()) X = (Y).begin(); X != (Y).end(); ++X)

#define debug(x) cout << '>' << #x << ':' << x << endl;

typedef long long int64;

typedef vector <int> vi;
typedef vector < vi > vvi;


typedef pair<pair<int, int>, pair<int, int> > Rect;


int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

	int testCount;
    cin >> testCount;

    for (int testNumber = 1; testNumber <= testCount; ++testNumber) {
        int n;
        cin >> n;
        
        vector<int> a(n);
        for (int i =0 ; i < n; ++i)
            cin >> a[i];

        vector<pair<int, int> > pairs(n);
        for (int i = 0; i < n; ++i) {
            pairs[i] = make_pair(a[i], i);
        }
        sort(all(pairs));
        reverse(all(pairs));
        int res = 0;
        for (int i = 1; i < n; ++i) {
            int pos = pairs[i].second;
            int left = 0, right = 0;
            for (int j = 0; j < i; ++j) {
                if (pairs[j].second < pos)
                    left++;
                else
                    right++;
            }
            res += min(left, right);
        }
        
        cout << "Case #" << testNumber << ": " << res << endl;
    }

    return 0;
}
