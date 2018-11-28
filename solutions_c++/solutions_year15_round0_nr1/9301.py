#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

#define get getchar()//_unlocked()

inline int scan()
{
	int n = 0, ch = get;

	while (ch < 48 || ch > 57)
		ch = get;
	while (ch >= 48 && ch <= 57) {
		n = (n<<3) + (n<<1) + ch - 48;
		ch = get;
	}

	return n;
}

int main()
{
    freopen("LOLA.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, n ,i, j, k, l, ans;
	char s[1000001];
	t = scan();
	j = t;
	while (t--) {
		scanf("%d", &n);
		getchar();
		scanf("%[^\n]s", s);
		l = strlen(s);
		ans  = k = 0;
		for (i = 0; i < l; i++) {
			if (k < i) {
				ans += i-k;
				k +=s[i]-48+i-k;
			}
			else {
				k += s[i]-48;
			}
		}
		printf("Case #%d: %d\n", j-t, ans);
	}
	return 0;
}
