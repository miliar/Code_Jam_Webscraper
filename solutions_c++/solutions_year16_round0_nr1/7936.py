#include <bits/stdc++.h>
using namespace std;

vector<bool> nums;

bool isAllOnes() {
	for (int i = 0; i < nums.size(); ++i) {
		if (!nums[i]) {
			return false;
		}
	}
	return true;
}

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	long long t, n;
	cin >> t;
	for (int tc = 0; tc < t; ++tc) {
		cin >> n;
//		n = tc+1;
		if(!n)
		{
			cout << "Case #" << tc+1 <<": " << "INSOMNIA" << endl;
			continue;
		}
		nums.assign(10, false);
		long long base=0,nn = n;
		while (!isAllOnes()) {
			base +=n;
			nn = base ;
//			cout << nn <<endl;
			do {
				nums[nn % 10] = true;
				nn /= 10;
			} while (nn);

		}
		if (isAllOnes()) {
			cout << "Case #" << tc+1 <<": " << base << endl;
		}
	}
	return 0;
}
