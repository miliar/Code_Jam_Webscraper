#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large_out.out", "w", stdout);
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		string str;
		int cnt = 0;
		cin >> str;
		for (int i = 1; i < str.length(); ++i)
			if (str[i] != str[i - 1])
				cnt++;
		if (str[str.length() - 1] == '-')
			cnt++;
		printf("Case #%d: %d\n", i, cnt);
	}
}