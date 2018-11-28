#include <iostream>
#include <string>
using namespace::std;

main ()
{
	int T;
	cin >> T;

	for (int t = 0; t < T; ++t)
	{
		int sMax;
		cin >> sMax;

		string s;
		cin >> s;

		int n = 0;
		int count = 0;
		for (int i = 0; i < s.size(); ++i)
		{
			int curr = s[i] - '0';
			if (curr > 0)
			{
				if (n < i)
				{
					count += (i - n);
					n = curr + i;
				}
				else
					n += curr;
			}
		}

		cout << "Case #" << t + 1 << ": " << count << endl;
	}
}
