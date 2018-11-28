#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int tail, result;
char s[102];

void rotate(int x, int y)
{
	char temp;
	int i = x, j = y;
	if (x > y)
		return;
	while (i < j) {
		temp = s[i]; s[i] = s[j]; s[j] = temp;
		s[i] = ((s[i] == '-') ? '+' : '-');
		s[j] = ((s[j] == '-') ? '+' : '-');
		i++;
		j--;
	}
	if (i == j) {
		s[i] = ((s[i] == '-') ? '+' : '-');
		i++;
		j--;
	}
	result++;
}

int main()
{
	int t, l;
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	cin >> t;
	for (int times = 1; times <= t; times++) {
		cin >> s;
		result = 0;
		tail = strlen(s) - 1;
		while (tail >= 0 && s[tail] == '+')
			tail--;
		while (tail >= 0) {
			l = 0;
			while (l <= tail && s[l] == '+')
				l++;
			rotate(0, l - 1);
			rotate(0, tail);
			while (tail >= 0 && s[tail] == '+')
				tail--;
		}
		printf("Case #%d: %d\n", times, result);
	}
	return 0;
}
