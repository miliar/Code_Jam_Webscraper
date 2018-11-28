#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	int t, n, cases = 1, counter = 1;
	string s;
	vector<char> v;

	cin >> t;

	while (cases <= t)
	{
		
		cin >> n;
		counter = 1;

		if (n == 0)
		{
			cout << "Case #" << cases << ": INSOMNIA" << endl;
			cases++;
			continue;
		}

		while (v.size() < 10)
		{
			s = to_string(n * counter);
			counter++;

			for (int i = 0; i < s.length(); i++)
			{
				if (find(v.begin(), v.end(), s[i]) == v.end())
				{
					v.push_back(s[i]);
				}
			}
		}

		v.clear();
		cout << "Case #" << cases << ": " << s << endl;
		cases++;
	}

	return 0;
}