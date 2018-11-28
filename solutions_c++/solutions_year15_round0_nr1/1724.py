#include <iostream>
#include <string>
using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int Tn, T;
	cin >> Tn;
	for (T=1;T<=Tn;T++) {
		int smax;
		string nums;
		cin >> smax >> nums;
		int ans = 0;
		int stand = 0;
		for (int i=0;i<=smax;i++) {
			int x = nums[i] - '0';
			if (stand < i) {
				ans += i-stand;
				stand = i;
			}
			stand += x;
		}
		cout << "Case #" << T << ": " << ans << endl;
	}
}