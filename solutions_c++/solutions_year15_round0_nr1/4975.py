#include <iostream>
#include <algorithm>
using namespace std;

int main(int argc, char* argv[]) {
	freopen("A-large.in","r",stdin); freopen("StandingOvation.out","w",stdout);
	int T;
	cin >> T;
	for (int aaa = 1; aaa <= T; aaa++) {
		int m;
		cin >> m;
		string s;
		cin >> s;
		int sum = 0;
		int ans = 0;
		for (int i = 0; i < s.size(); i++) {
			ans = max(ans, i - sum);
			sum += s[i] - '0';
		}
		cout << "Case #" << aaa << ": " << ans << "\n";
	}

	return 0;
}

