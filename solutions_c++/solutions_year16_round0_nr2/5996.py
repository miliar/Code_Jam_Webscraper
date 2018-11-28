#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;


int main()
{
	FILE *f1, *f2;
	freopen_s(&f1, "in.txt", "r+", stdin);
	freopen_s(&f2, "out.txt", "w+", stdout);
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		string S;
		char pos = '+';
		int ans = 0;
		cin>>S;
		for (int i = S.length() - 1; i >= 0; i--)
		{
			if (pos != S[i])
			{
				pos = S[i];
				ans++;
			}
		}
		printf("Case #%d: %d\n", i, ans);
	}
	return 0;
}

