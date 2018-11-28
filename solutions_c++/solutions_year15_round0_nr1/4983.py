#include<iostream>
#include<string>

using namespace std;

void main()
{
	int T, S, total, extra, len, i, n;
	string s;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cin >> S;
		cin >> s;
		total = 0;
		extra = 0;
		len = s.length();
		for (i = 0; i < len; i++)
		{
			n = s[i] - 48;
			if (total < i)
			{
				extra += i - total;
				total += i - total;
			}
			total += n;
		}
		cout << "Case #" << t << ": " << extra << endl;
	}
}