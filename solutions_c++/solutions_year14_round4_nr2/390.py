#pragma comment(linker, "/STACK:1000000000")
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

#define pb push_back
#define mp make_pair
#define fs first
#define sc second

const double pi = acos(-1.0);
const int size = 2 * 1000;
const int inf = 1000 * 1000 * 1000;

int val[size];
int invf[size];
int invb[size];
int n;
int tc;
int f[size][size];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> tc;
    for (int tnum = 0; tnum < tc; tnum++) {
    	cin >> n;
    	for (int i = 0; i < n; i++) {
    		cin >> val[i];
    	}
    	int ans = 0;
    	for (int i = 0; i < n; i++) {
    		int c1 = 0, c2 = 0;
    		for (int j = 0; j < n; j++)
    			if (val[j] > val[i]) {
    				if (j < i)
    					c1++;
    				else
    					c2++;
    			}
    		ans += min(c1, c2);
    	}

        cout << "Case #" << tnum + 1 << ": " << ans << endl;
    }

    return 0;
}