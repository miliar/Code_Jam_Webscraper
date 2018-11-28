#include <bits/stdc++.h>

inline void flip(char &ch)
{
	if (ch == '-')
		ch = '+';
	else
		ch = '-';
}

int main()
{
	std::ios::sync_with_stdio(false);
	int T;
	std::cin >> T;
	for (int Case = 1; Case <= T; Case ++)
	{
		std::cout << "Case #" << Case << ": ";
		std::string s;
		std::cin >> s;
		int cnt = 0;
		for (int i = (int)s.length() - 1; i >= 0; i --)
			if (s[i] == '-')
			{
				cnt ++;
				for (int j = 0; j <= i; j ++)
					flip(s[j]);
			}
		std::cout << cnt << std::endl;
	}
	return 0;
}
