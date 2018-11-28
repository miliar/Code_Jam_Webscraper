// Problem B. Revenge of the Pancakes
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
	int T;
	cin >> T;
	for (int ti = 1; ti <= T; ti++) {
		static char s[1024];
		scanf("%s\n", s);
		int n = strlen(s);
		for (int i = n - 1; i >= 0; i--)
			if (s[i] == '+') s[i] = '\0';
			else break;
		n = strlen(s);
		int ans = 0;
		for (int i = 0, j = 0; i < n; i++)
			if (s[i] != j) {
				ans++;
				j = s[i];
			}

		printf("Case #%d: %d\n", ti, ans);
	}

	return 0;
}
