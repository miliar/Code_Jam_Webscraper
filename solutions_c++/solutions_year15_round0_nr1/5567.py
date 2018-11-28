#include <bits/stdc++.h>

using namespace std;

int num(char c) {
	return c - '0';
}

int main(int argc, char const *argv[])
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t)
	{
		int standing = 0;
		int k;
		int res = 0;
		char s[2000];
		scanf("%d %s", &k, s);
		int l = strlen(s);

		standing += num(s[0]);

		for (int i = 1; i < l; ++i)
		{
			if (num(s[i]) && standing < i) {
				res += (i - standing);
				standing += (i-standing);
			}
			standing += num(s[i]);
		}

		printf("Case #%d: %d\n", t, res);
	}

	return 0;
}