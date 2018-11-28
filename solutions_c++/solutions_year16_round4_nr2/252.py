#include <iostream>
#include <iomanip>
#include <string>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <ctime>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <bitset>
#include <algorithm>
#include <utility>
#include <complex>

using namespace std;
typedef long long ll;
typedef double ld;

typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef complex<ll> pt;

ld p[1<<8];
ld prob[1<<8];
ld prob2[1<<8];

int main(){
	int tt; cin >> tt;
	for (int zz = 1; zz <= tt; zz++){
		int n; cin >> n;
		int k; cin >> k;
		for (int i = 0; i < n; i++)
			cin >> p[i];
		sort(p,p+n);
		//cout << "n = " << n << ", k = " << k << endl;
		
		ld best = 0;
		
		for (int beg = 0; beg < k; beg++){
			int end = k - 1 - beg;
			
			for (int i = 1; i <= k/2; i++)
				prob[i] = 0.;
			prob[0] = 1.;
			for (int i = 0; i < beg; i++){
				for (int j = k/2; j > 0; j--){
					prob[j] = prob[j] * (1-p[i]) + prob[j-1] * p[i];
				}
				prob[0] = prob[0] * (1-p[i]);
			}
			for (int i = n - end; i < n; i++){
				for (int j = k/2; j > 0; j--){
					prob[j] = prob[j] * (1-p[i]) + prob[j-1] * p[i];
				}
				prob[0] = prob[0] * (1-p[i]);
			}
			for (int i = beg; i < n-end; i++){
				ld ans = prob[k/2] * (1-p[i]) + prob[k/2-1] * p[i];
				best = max(best, ans);
			}
		}
		
		printf("Case #%d: %.9f\n", zz, best);
		
	}
	
	return 0;
}
