#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <cstdio>
#include <string>

using namespace std;

string get_next(string s)
{
	int ps = s.length() - 2;
	while (s[ps] == '1') 
		s[ps--] = '0';
	s[ps] = '1';
	return s;
}

long long int convert_from2decimal(string s, long long int base) {
	long long res = 0;
	for (auto i = 0; i < s.length(); i++)
		res = res*base + (long long int)(s[i] - '0');
	return res;
}

bool check(string s, vector<long long int>& d) {
	for (long long int k = 2; k <= 10; k++) {
		long long int v = convert_from2decimal(s, k);
		bool ok = false;
		for (long long int j = 2; !ok && j<= (long long int)(sqrt(v+0.5)); j++)
			if (v % j == 0) {
				ok = true;
				d[k - 2] = j;
			}
		if (!ok)
			return false;
	}
	return true;
}

int main()
{
	//freopen("B-large.in", "r", stdin); 
	freopen("C-1.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		int n, j, cnt = 0;
		cin >> n >> j;
		cout << "Case #" << t << ": " << endl;
		vector<long long int> div(9, 0);
		string s = "1";
		for (int i = 0; i < n - 2; i++)
			s += '0';
		s += '1';

		while (cnt < j) {
			s = get_next(s);
			if (check(s, div)) {
				cnt++;
				cout << s;
				for (auto i = 0; i < div.size(); ++i)
					cout << " " << div[i];
				cout << endl;
			}
		}
	}
	//system("pause");
	return 0;
}