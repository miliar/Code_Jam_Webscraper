#include <iostream>
#include <vector>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int icase = 1; icase <= T; ++ icase) {
		string s;
		cin >> s;
		vector<char> stack(1, s[0]);
		int p = 0;
		while (p < s.size()) {
			if (stack.back() != s[p]) {
				stack.push_back(s[p]);
			}
			++ p;
		}
		int res = 0;
		if (stack.back() == '-') ++ res;
		stack.pop_back();
		res += stack.size();
		cout << "Case #" << icase << ": " << res << endl;
	}
	return 0;
}
