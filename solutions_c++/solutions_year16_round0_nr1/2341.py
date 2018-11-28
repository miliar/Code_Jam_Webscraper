#include <iostream>
#include <sstream>
#include <unordered_set>
#include <vector>

using namespace std;

int main() {
	int64_t Ncase;
	cin >> Ncase;
	ostringstream output;
	for (int64_t i1 = 1; i1 <= Ncase; ++i1){
		int64_t N;
		cin >> N;
		if(N == 0) {
			output << "Case #" << i1 << ": " << "INSOMNIA" << endl;
			continue;
		}
		unordered_set<int> nums({0,1,2,3,4,5,6,7,8,9});
		int64_t i2 = 1;
		while (!nums.empty()) {
			int64_t multiple = N*i2++;
			vector<int> digits;
			int d;
			while (multiple > 0) {
				d = multiple % 10;
				multiple /= 10;
				nums.erase(d);
			}
		}
		output << "Case #" << i1 << ": " << N*(i2-1) << endl;
	}
	cout << output.str();
	return 0;
}
