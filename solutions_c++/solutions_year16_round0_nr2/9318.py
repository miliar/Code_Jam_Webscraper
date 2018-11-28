#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;
bool v[105];
int n;
int get_bad()
{
	for (int i = n - 1; i >= 0; i--)
	{
		if (!v[i])
			return i;
	}
	return -1;
}

int get_last_plus()
{
	for (int i = 0; i < n; i++)
	{
		if (!v[i])
			return i - 1;
	}
}

void reverse(int f)
{
	for (int i = 0; i < f; i++, f--)
	{
		swap(v[i], v[f]);
	}
}

int main()
{
	//ifstream cin("input.txt");
	//ofstream cout("output.txt");
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		fill(v, v + 105, false);
		string s;
		cin >> s;
		n = s.size();
		for (int j = 0; j < s.size(); ++j)
		{
			v[j] = s[j] == '+';
		}
		int ans = 0;

		int bad = get_bad();

		while (bad != -1)
		{
			int first_last_plus = get_last_plus();
			if (first_last_plus != -1)
			{
				ans++;
				for (int j = 0; j <= first_last_plus; ++j)
				{
					v[j] = !v[j];
				}
			}
			ans++;
			for (int k = 0; k <= bad; ++k)
			{
				v[k] = !v[k];
			}
			reverse(bad);
			bad = get_bad();
		}
		cout << "Case #" << i << ": " << ans << endl;

	}

	return 0;
}