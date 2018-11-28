#include <algorithm>
#include <iostream>
#include <set>
#include <vector>
using namespace std;

bool isupdown(const vector<int>& v) {
	bool goingup = true;
	for (int i = 1; i < v.size(); i++) {
		if (v[i] > v[i-1] && goingup) continue;
		if (v[i] < v[i-1] && goingup) {
			goingup = false;
			continue;
		}
		if (v[i] < v[i-1] && !goingup) continue;
		return false;
	}
	return true;
}

int main() {
	vector<int> nums;
	int T, N;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		cin >> N;
		nums.resize(N);
		set<vector<int> > numbuf;
		for (int n = 0; n < N; n++) cin >> nums[n];
		numbuf.insert(nums);
		int swaps = 0;
		for(;;) {
			int done = false;
			for (const vector<int>& v : numbuf) {
				if (isupdown(v)) {
					done = true;
					break;
				}
			}
			if (done) break;
			set<vector<int> > newnumbuf;
			swaps++;
			for (const vector<int>& v : numbuf) {
				for (int i = 1; i < N; i++) {
					vector<int> v2 = v;
					swap(v2[i-1], v2[i]);
					newnumbuf.insert(v2);
				}
			}
			numbuf = move(newnumbuf);
		}
		cout << "Case #" << tc << ": " << swaps << endl;
	}
}
