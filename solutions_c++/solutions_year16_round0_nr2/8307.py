#include <iostream>
#include <vector>

using namespace std;

int flips(string s)
{
	int res = 0;
	int i = 0;
	int n = s.size();
	while (i < n) {
		while (i + 1 < n && s[i] == s[i+1]) i++;
		if (i == n - 1) {
			if (s[i] == '-') res++;
			break;
		}
		res++;
		i++;
	}
	return res;
}

int main()
{
	int T;
	cin >> T;
	vector<int> res;

	while (T--) {
		string s;
		cin >> s;
		res.push_back(flips(s));
	}
	for (int i = 0; i < res.size(); i++)
		cout << "Case #" << i+1 << ": " << res[i] << endl;
	return 0;
}
