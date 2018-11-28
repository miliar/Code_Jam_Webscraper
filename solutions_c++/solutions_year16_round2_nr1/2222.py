#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
	int t, a[256], num[10];
	string s;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin >> t;
	for (int times = 1; times <= t; times++) {
		cin >> s;
		memset(a, 0, sizeof(a));
		memset(num, 0, sizeof(num));
		for (int i = 0; i < s.length(); i++)
			a[s[i]]++;
		num[0] = a['Z'];
		num[1] = a['O'] - a['Z'] - a['W'] - a['U'];
		num[2] = a['W'];
		num[3] = a['H'] - a['G'];
		num[4] = a['U'];
		num[5] = a['V'] - a['S'] + a['X'];
		num[6] = a['X'];
		num[7] = a['S'] - a['X'];
		num[8] = a['G'];
		num[9] = (a['N'] - num[1] - num[7]) / 2;
		printf("Case #%d: ", times);
		for (int i = 0; i < 10; i++)
			for (int j = 0; j < num[i]; j++)
				printf("%d", i);
		printf("\n");
	}
	return 0;
} 
