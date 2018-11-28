#include <iostream>
#include <cstdio>
#include <cstring> 
using namespace std;

int found, t, n, j;
char s[34], rs[500][34];
long long value, mod, r[500][11];

void baseConvert(int base)
{
	long long p = 1;
	value = 0;
	for (int i = n - 1; i >= 0; i--) {
		if (s[i] == '1')
			value += p;
		p *= base;
	}
}

void fastPower(long long p)
{
	if (p == 1) {
		mod = 2;
		return;
	}
	if (p % 2 == 0) {
		fastPower(p / 2);
		mod = (mod * mod) % value;
	}
	else {
		fastPower(p / 2);
		mod = (mod * mod) % value;
		mod = (mod * 2) % value;
	}
}

bool checkPrime(int base)
{
	//fastPower(value - 1);
	//if (mod == 1)
	//	return true;
	for (long long i = 2; i * i <= value; i++)
		if (value % i == 0) {
			r[found][base] = i;
			return false;
		}
	return true;
}

void find(int pos)
{
	if (pos == n - 1) {
		if (found == j)
			return;
		strcpy(rs[found], s);
		for (int i = 2; i <= 10; i++) {
			baseConvert(i);
			if (checkPrime(i))
				return;
		}
		/*printf("%s", s);
		for (int i = 2; i <= 10; i++)
			printf(" %I64d", r[found][i]);
		printf("\n");*/
		found++;
		return;
	}
	s[pos] = '0';
	find(pos + 1);
	s[pos] = '1';
	find(pos + 1);
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	cin >> t;
	for (int times = 1; times <= t; times++) {
		cin >> n >> j;
		found = 0;
		memset(s, 0, sizeof(s));
		memset(r, 0, sizeof(r));
		s[0] = '1';
		s[n - 1] = '1';
		find(1);
		printf("Case #%d: \n", times);
		for (int i = 0; i < j; i++) {
			printf("%s", rs[i]);
			for (int k = 2; k <= 10; k++)
				printf(" %lld", r[i][k]);
			printf("\n");
		}
	}
	return 0;
}
