#include <iostream>
#include <sstream>
#include <unordered_set>
#include <vector>
#include <unordered_map>

using namespace std;

int main() {
	int64_t Ncase;
	cin >> Ncase;
	ostringstream output;
	for (int64_t i1 = 1; i1 <= Ncase; ++i1){
		string instr;
		cin >> instr;
		int N = instr.length();

		unordered_map <char, int> f;

		for (int i = 0; i < N; ++i) {
			f[instr[i]]++;
		}
// Z 0, W 2, V - n5 = 7s, X 6, U 4, F - n4 = n5, G 8, 
		// 1 3 9
		vector<int> nums(10,0);

		nums[0] = f['Z'];
		nums[2] = f['W'];
		nums[6] = f['X'];
		nums[4] = f['U'];
		nums[8] = f['G'];
		nums[5] = f['F'] - nums[4];
		nums[7] = f['V'] - nums[5];
		nums[9] = f['I'] - nums[5] - nums[6] - nums[8];
		nums[3] = f['H'] - nums[8];
		nums[1] = f['N'] - nums[9] * 2 - nums[7];

		vector<int> ans;
		for (int i = 0; i < 10; ++i) {
			while(nums[i]-- > 0) {
				ans.push_back(i); // Cast
			}
		}
		cout << "Case #" << i1 << ": ";
		for (int i = 0; i < ans.size(); ++i) {
			cout << ans[i];
		}
		cout << endl;
	}
	cout << output.str();
	return 0;
}
