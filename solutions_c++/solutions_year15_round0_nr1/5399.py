#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
#define pi 3.14159265359

char s[1111] = { 0 };

int main()
{
	FILE **file = new FILE*;
	freopen_s(file, "input.txt", "r", stdin);
	freopen_s(file, "output.txt", "w", stdout);
	int t;
	cin >> t;
	int smax;
	int res, kol, temp;
	for (int i = 0; i < t; ++i)
	{
		cin >> smax;
		cin >> s;
		res = 0, kol=0;
		for (int j = 0; j <= smax; ++j)
		{
			if (s[j] == '0')
				continue;
			if (kol < j)
			{
				temp = j - kol;
				kol += temp;
				res += temp;
			}
			kol += s[j] - '0';
		}
		cout << "Case #" << i + 1 << ": " << res << "\n";
	}

	return 0;
}