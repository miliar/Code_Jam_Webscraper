#include <iostream>
#include <string>

using namespace std;

static int Solve(string& s)
{
	int ret = 0;
	while (s.find("-") != string::npos) {
		auto next = s[0] == '+' ? '-' : '+';
		for (auto& c : s){
			if (c == next) break;
			c = next;
		}
		ret++;
	}
	return ret;
}

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		string s;
		cin >> s;
		cout << "Case #" << t + 1 << ": " << Solve(s) << endl;
	}
	return 0;
}