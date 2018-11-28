#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int k = 0; k < t; k++)
	{
		int smax;
		cin >> smax;
		string s;
		cin >> s;
		int sum = 0, max = 0;
		for (int i = 0; i < s.length(); i++)
		{
			if (sum < i)
				if (max < i - sum)
					max = i - sum;
			sum += s[i] - '0';
		}
		cout << "Case #" << k + 1 << ": " << max << endl;
	}
	return 0;
}