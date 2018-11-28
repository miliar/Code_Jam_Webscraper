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
    	vector<bool> good(17, true);

        for (int i = 0; i < 2; ++i) {
            int answer;
            cin >> answer;
            vector<vector<int> > cards(4, vector<int>(4));
            for (int j = 0; j < 4; ++j) {
                for (int k = 0; k < 4; ++k) {
                    cin >> cards[j][k];
                }
            }
            vector<int>& vec = cards[answer - 1];
            for (int c = 1; c < good.size(); ++c) {
                if (good[c] && find(vec.begin(), vec.end(), c) == vec.end())
                    good[c] = false;
            }
        }

        int good_index = -1;
        string res = "Volunteer cheated!";
        for (int c = 1; c < good.size(); ++c) {
            if (good[c]) {
                if (good_index < 0) {
                    good_index = c;
                } else {
                    good_index = -1;
                    res = "Bad magician!";
                    break;
                }
            }
        }
        if (good_index == -1)
		  cout << "Case #" << testNumber << ": " << res << endl;
        else
          cout << "Case #" << testNumber << ": " << good_index << endl;

    }

    return 0;
}
