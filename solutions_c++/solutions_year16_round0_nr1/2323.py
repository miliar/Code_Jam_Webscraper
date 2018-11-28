#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

string to_str(long long x) {
	stringstream ss;
	ss << x;
	string ans;
	ss >> ans;
	return ans;
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		long long x;
		cin >> x;
		if (x == 0) {
			cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
			continue;
		}
		vector<bool> used(10);
		int cnt = 1;
		long long ans;
		while (find(used.begin(), used.end(), false) != used.end()) {
			long long nx = cnt * x;
			string s = to_str(nx);
			for (int j = 0; j < int(s.size()); j++) {
				used[s[j] - '0'] = true;
			}
			ans = nx;
			cnt++;
		}
		cout << "Case #" << i + 1 <<  ": " << ans << endl;
	}
    return 0;
}

