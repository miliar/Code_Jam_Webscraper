#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>

using namespace std;

int main()
{
	freopen("C:/temp/in.txt", "r",stdin);
	freopen("C:/temp/out.txt", "w", stdout);
	int T;
	cin >> T;
	for (int i = 0; i < T;i++)
	{
		int Smax;
		string s;
		cin >> Smax >> s;
		int c = 0;
		int tc = 0;
		for (int j = 0; j <= Smax; j++)
		{
			if ((s[j] - '0') && j>tc)
			{
				c += (j - tc);
				tc += (j - tc);
			}
			tc += (s[j] - '0');
			
		}
		printf("Case #%d: %d\n", i + 1, c);
	}
}