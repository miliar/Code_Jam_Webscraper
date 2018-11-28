#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

bool isVowel(char c)
{
	return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		string s;
		int n;
		cin >> s >> n;

		map<int, int> ind;
		for (int i = 0; i < s.size(); i++)
		{
			char c = s[i];
			if (!isVowel(c))
			{
				int start = i, j = 0;
				while (start + j < s.size() && !isVowel(s[start + j]))
				{
					j++;
				}

				if (j >= n)
				{
					ind[start] = j;
				}

				i += j;
			}
		}

		unsigned long long r = 0;
		int last = -1;
		for (map<int, int>::iterator it = ind.begin(); it != ind.end(); it++)
		{
			int i = it->first;
			int l = it->second;
			for (int j = 0; j <= l - n; j++)
			{
				unsigned long long a = i + j - (last + 1) + 1;
				unsigned long long b = s.size() - (i + j + n) + 1;
				r += a * b;
				last = i + j;
			}
		}

		cout << "Case #" << t + 1 << ": " << r << endl;
	}
	return 0;
}