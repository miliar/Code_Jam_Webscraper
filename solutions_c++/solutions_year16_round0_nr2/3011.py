#include <iostream>
#include <cstring>
#include <cstdio>
#define DIM 150

using namespace std;

int t, n, rez;
char s[DIM];

int done()
{
    char cap = s[0];
    if (cap != '+') return 0;
    for (int i = 0; s[i]; i++)
		if (s[i] != cap)
			return 0;
	return 1;
}

void solve()
{
	for (rez = 0; !done(); rez++) {
        char cap = s[0];
        int i = 1;
        for (; s[i] && s[i] == cap; i++);
        for (int j = 0; j < i; j++)
			if (s[j] == '+') s[j] = '-';
			else s[j] = '+';
	}
}

int main()
{
    freopen("pan.in", "r", stdin);
    freopen("pan.out", "w", stdout);

	scanf("%d\n", &t);
	for (int i = 1; i <= t; i++)
	{
        fgets(s, DIM, stdin);
        s[strlen(s)-1] = 0;
        printf("Case #%d: ", i);
		solve();
		printf("%d\n", rez);
	}

    return 0;
}
