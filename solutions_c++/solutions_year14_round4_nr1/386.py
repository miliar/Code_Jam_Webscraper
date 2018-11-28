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
const int size = 100 * 1000;

int n, x;
int w[size];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int tc;
    cin >> tc;
    for (int tnum = 0; tnum < tc; tnum++) {
    	cerr << tnum + 1 << endl;
    	cin >> n >> x;
    	for (int i = 0; i < n; i++)
    		cin >> w[i];
    	sort(w, w + n);

    	for (int i = 0; i <= n; i++) {
    		if ((n - i) & 1)
    			continue;
    		bool flag = true;
    		for (int j = 0; j < (n - i) / 2; j++)
    			if (w[j] + w[n - 1 - i - j] > x) {
    				flag = false;
    				break;
    			}
    		if (flag) {
    	    	cout << "Case #" << tnum + 1 << ": " << i + (n - i) / 2 << endl;
    	    	break;
    		}
    	}
    }

    return 0;

}