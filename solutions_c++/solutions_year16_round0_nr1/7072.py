#include <bits/stdc++.h>
using namespace std;

vector<int> breaknum(int a) {
	vector<int> nums;
	if(a == 0) {
		nums.push_back(0);
	} else {
		while(a != 0) {
			int b = a%10;
			a = a/10;
			nums.push_back(b);
		}
		reverse(nums.begin(), nums.end());
	}
	return nums;
}

int main() {
	int t, ans, n;
	scanf("%d", &t);
	for(int i = 0; i < t; i++) {
		map <int, bool> nums;
		bool seen[10] = {false};
		ans = -1;
		scanf("%d", &n);
		int j = 1;
		while(true) {
			int num = j*n;
			bool done = true;
			if(nums[num]) {
				ans = -1;
				break;
			} else {
				nums[num] = true;
				vector<int> split = breaknum(num);
				for(int k = 0; k < split.size(); k++) {
					seen[split[k]] = true;
				}
			}
			for(int k = 0; k < 10; k++) {
				if(!seen[k]) done = false;
			}
			if(done) {
				ans = num;
				break;
			}
			j++;
		}
		if(ans == -1) printf("Case #%d: INSOMNIA\n", i+1);
		else printf("Case #%d: %d\n", i+1, ans);
	}
}