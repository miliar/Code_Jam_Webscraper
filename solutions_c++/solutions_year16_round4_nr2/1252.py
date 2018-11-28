#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <cstring>
#include <cmath>
using namespace std;
#define MAXN 1000000
typedef long long int ll;
typedef pair<int,int> pii;
typedef long double ld;

int n, k;
ld p[200];

ld C(int n, int k) {
    ld r = 1.0;
    for (int i = 0; i < k; i++) {
        r *= n - i;
        r /= i + 1;
    }
    return r;
}

int main() {
	ios_base::sync_with_stdio(0);
	
	//freopen("B.test.in", "r", stdin);
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small.out", "w", stdout);

	int testcases;
	cin >> testcases;

	for (int testcase = 1; testcase <= testcases; testcase++) {
		cout << "Case #" << testcase << ": ";
		
		cin >> n >> k;
		
		for (int i = 0; i < n; i++) {
            cin >> p[i];
		}
		
		ld res = 0;
		int ctr = 0;
		
		for (int m = 0; m < (1 << n); m++) {
            if (__builtin_popcount(m) == k) {
                ctr++;
                ld sum = 0;
                for (int mask = 0; mask < (1 << k); mask++) {
                    if (__builtin_popcount(mask) == (k >> 1)) {
                        ld prob = 1;
                        for (int i = 0, j = 0; i < n; i++) {
                            if (m & (1 << i)) {
                                if (mask & (1 << j)) {
                                    prob *= p[i];
                                } else {
                                    prob *= 1.0 - p[i];
                                }
                                j++;
                            }
                        }
                        sum += prob;
                        
//                        cout << m << " " << mask << " " << prob << endl;
                    }
                }
                
                res = max(res, sum );
            }
		}
		
		cout << res << endl;
	}

	return 0;
}

