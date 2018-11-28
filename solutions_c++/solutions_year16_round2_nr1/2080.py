#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

void solve(int t)
{
	string s;
	cin >> s;

	vector<int> ch(256);

	for (int i = 0; i < s.length(); ++i)
		++ch[s[i]];

	vector<int> digits(10);

	digits[0] = ch['Z'];
	digits[2] = ch['W'];
	digits[4] = ch['U'];
	digits[6] = ch['X'];
	digits[8] = ch['G'];

	digits[3] = ch['H'] - digits[8];
	digits[5] = ch['F'] - digits[4];
	digits[7] = ch['V'] - digits[5];
	digits[1] = ch['O'] - digits[0] - digits[2] - digits[4];
	digits[9] = ch['I'] - digits[5] - digits[6] - digits[8];

	// for(int i = 0; i < 10; ++i)
	// {
	// 	cout << digits[i] << endl;
	// }
	string res;
	for (int i = 0; i < 10; ++i)
		res += string(digits[i], '0' + i);
	cout << "Case #" << t + 1 << ": " << res << endl;
}

int main(int argc, char* argv[])
{
	int t;
	cin >> t;

	for (int i = 0; i < t; ++i)
	{
		solve(i);
	}
	return 0;
}
