#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
#include <cmath>
using namespace std;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int Tn, T;
	cin >> Tn;
	for (T=1;T<=Tn;T++) {
		int d;
		vector<int> nums;		
		cin >> d;
		for (int i=0;i<d;i++) {
			int tmp;
			cin >> tmp;
			nums.push_back(tmp);
		}
		sort(nums.begin(), nums.end(), greater<int>());
		int ans = nums[0];

		for (int i=1;i<=nums[0];i++) {
			int tmp = 0, m = 0;
			for (int j=0;j<nums.size();j++) {
				int div = ceil((double)nums[j]/i);
				m = max(m, (int)ceil((double)nums[j]/div));
				tmp += div-1;
			}
			ans = min(ans, tmp+m);
		}

		cout << "Case #" << T << ": " << ans << endl;
	}
}