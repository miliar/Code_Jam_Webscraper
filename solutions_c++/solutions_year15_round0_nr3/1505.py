#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
using namespace std;

int arr[5][5] = {	0, 0, 0, 0, 0,
					0, 1, 2, 3, 4,
					0, 2, -1, 4, -3,
					0, 3, -4, -1, 2,
					0, 4, 3, -2, -1 };

const int N = 10005;
char s[N], s1[N], s2[N];

inline int sgn(int x)
{
	return x < 0 ? -1 : 1;
}

int main()
{
	//freopen("input.txt", "r", stdin);
	freopen("C-small-attempt2.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for (int tt = 1; tt <= T; ++tt)
	{
		int l, x;
		cin >> l >> x;
		scanf("%s", s);
		for (int i = 1; i < x; ++i)
			for (int j = 0; j < l; ++j)
				s[i*l + j] = s[j];
		int n = l * x;
		s[n] = 0;

		for (int i = 0; i < n; ++i)
			s[i] = s[i] - 'i' + 2;
		memcpy(s1, s, n + 1);
		memcpy(s2, s, n + 1);

		bool ans = 0;
		int i1 = -1, i2 = -1;
		if (s[0] == 2)
			i1 = 0;
		else
			for (int i = 1; i < n; ++i)
			{
				s[i] = sgn(s[i - 1]) * sgn(s[i]) * arr[abs(s[i - 1])][abs(s[i])];
				if (s[i] == 2)
				{
					i1 = i;
					break;
				}
			}
		if (s1[n - 1] == 4)
			i2 = n - 1;
		else
			for (int i = n - 2; i >= 0; --i)
			{
				s1[i] = sgn(s1[i + 1]) * sgn(s1[i]) * arr[abs(s1[i])][abs(s1[i+1])];
				if (s1[i] == 4)
				{
					i2 = i;
					break;
				}
			}
		if (i1 != -1 && i2 != -1 && i1 + 1 < i2)
		{
			for (int i = i1 + 2; i < i2; ++i)
				s2[i] = sgn(s2[i - 1]) * sgn(s2[i]) * arr[abs(s2[i - 1])][abs(s2[i])];
			ans = (s2[i2 - 1] == 3);
		}

		printf("Case #%d: %s\n", tt, ans ? "YES" : "NO");
	}

	return 0;
}