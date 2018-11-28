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

const int size = 10 * 1000 + 1000;
const int limit = 10 * 1000;
const long long inf = 1000 * 1000 * 1000;

int tc, n, k;
int sum[size];
int lb[size];
int rb[size];
bool used[size];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> tc;
    for (int tnum = 0; tnum < tc; tnum++) {
    	cin >> n >> k;
    	//cerr << n << ' ' << k << endl;
    	for (int i = 0; i < n - k + 1; i++)
    		cin >> sum[i];
    	for (int i = 0; i < n; i++)
    		used[i] = false;

    	for (int i = 0; i < k; i++) {
    		lb[i] = 0;
    		rb[i] = 0;
    		int p = i ;
    		int shift = 0;
    		while (p < n - k) {
    			shift += sum[p + 1] - sum[p];
    			lb[i] = min(lb[i], shift);
    			rb[i] = max(rb[i], shift);
    			//cerr << p << endl;
    			p += k;
    		}
    	}

  //  	cerr << "here" << endl;
    	long long ans = inf;
    	int llimit = limit;
    	for (int i = 0; i < k; i++)
    		llimit = max(llimit, abs(max(lb[i], rb[i])));
    	for (int i = -llimit * 2; i <= llimit * 2; i++) {
    		int clb = 0;
    		int crb = inf;
    		for (int j = 0; j < k; j++)
    			clb = max(clb, rb[j] - lb[j]);

    		while (clb < crb) {
//    			cerr << "here" << endl;
    			int mid = (clb + crb) / 2;
    			long long curmin = 0;
    			long long curmax = 0;
    			for (int j = 0; j < k; j++) {
    				curmin += i - lb[j];
    				curmax += i + mid - rb[j];		
    			}

    			if (sum[0] >= curmin && sum[0] <= curmax)
					crb = mid;
				else
					clb = mid + 1;
    		}

//    		cout << i << ' ' << clb << endl;
    		ans = min(ans, clb + 0ll);
    	}

    	cerr << tnum + 1 << endl;
    	cout << "Case #" << tnum + 1 << ": " << ans << endl;
    }

    return 0;
}