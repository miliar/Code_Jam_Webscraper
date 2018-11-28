#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>

using namespace std;

int solve(string);

int main()
{

	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int Tc;
	cin >> Tc;

	string str;
	for (int Tn = 1; Tn <= Tc; Tn++)
	{
		cin >> str;
		printf("Case #%d: %d\n", Tn, solve(str));
	}
	return 0;
}

int solve(string t)
{
	bool there_is_smth_to_do = true;
	int ans = 0;

	while (there_is_smth_to_do)
	{
		if (t.find('-') == string::npos) {
			return ans;
		}

		int l_ind = 0;
		while (t[l_ind] == '+') t[l_ind++] = '-';
	
		int r_ind = t.find_last_of('-');

		reverse(t.begin(), t.begin() + r_ind + 1);
		for (int i = 0; i <= r_ind; i++)
			t[i] = (t[i] == '+') ? '-' : '+';

		ans++;
		if (l_ind != !- 1)
			ans++;
	}
}