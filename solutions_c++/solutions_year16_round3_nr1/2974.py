#include <iostream>
#include <iomanip>
#include <cmath>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <climits>

using namespace std;

pair<char, char> remove_senators(vector<int>& a)
{
	if (all_of(a.begin(), a.end(), [](int x) {return x == 1; }) && count(a.begin(), a.end(), 1) % 2 == 1)
	{
		auto maximum = max_element(a.begin(), a.end());
		int f_max = distance(a.begin(), maximum);
		--(*maximum);
		char c1 = f_max + 65;
		return make_pair(c1, ' ');
	}
	auto maximum = max_element(a.begin(), a.end());
	int temp = *maximum;
	*maximum = 0;
	auto second_maximum = max_element(a.begin(), a.end());
	*maximum = temp;

	int f_max = distance(a.begin(), maximum);
	int s_max = distance(a.begin(), second_maximum);

	int s_max_prev_value = *second_maximum;

	--(*maximum);
	if(*second_maximum != 0) --(*second_maximum);

	char c1 = f_max + 65;
	char c2 = ' ';
	if (s_max_prev_value != 0) c2 = s_max + 65;
	return make_pair(c1, c2);
}

int main()
{
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for (unsigned xt = 1; xt <= t; ++xt)
	{
		cout << "Case #" << xt << ": ";

		int n;
		cin >> n;
		vector<int> a(n);
		for (int i = 0; i < n; ++i) cin >> a[i];
		while (!all_of(a.begin(), a.end(), [](int x) {return x == 0; }))
		{
			pair<char, char> temp = remove_senators(a);
			string s1(1, temp.first);
			string s2 = "";
			if (temp.second != ' ')
			{
				s2 = string(1, temp.second);
			}
			string s = s1 + s2;

			sort(s.begin(), s.end());
			cout << s << ' ';
		}
		cout << endl;
	}
}