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

string workers[1<<5];
string know[1<<5];

int n;

bool try_plan(int mask_work, int mask_machine){
	if (mask_machine == 0) return true;
	for (int i = 0; i < n; i++){
		if (!(mask_work & (1<<i))) continue;
		bool okay = false;
		for (int j = 0; j < n; j++){
			if (know[i][j] == '0') continue;
			if (!(mask_machine & (1<<j))) continue;
			okay = try_plan(mask_work - (1<<i), mask_machine - (1<<j));
			if (!okay) return false;
		}
		if (!okay) return false;
	}
	return true;
}

int main(){
	int tt; cin >> tt;
	for (int zz = 1; zz <= tt; zz++){
		cin >> n;
		for (int i = 0; i < n; i++)
			cin >> workers[i];
		int best = n*n;
		for (int mask = 0; mask < (1<<(n*n)); mask++){
			bool okay = true;
			int cnt = 0;
			for (int i = 0; i < n; i++){
				know[i] = workers[i];
			}
			for (int curr = 0; curr < (n*n); curr++){
				if (!(mask & (1<<curr))) continue;
				int i = curr/n, j = curr%n;
				if (workers[i][n] == '1'){
					okay = false;
					break;
				}
				know[i][j] = '1';
				cnt++;
			}
			if (okay){
				okay = try_plan((1<<n)-1,(1<<n)-1);
				if (okay) best = min(best,cnt);
			}
		}
		cout << "Case #" << zz << ": " << best << endl;
	}
	
	return 0;
}
