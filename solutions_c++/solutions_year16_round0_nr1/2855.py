#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int n, m;
char s[255];
bool d[10] = {false}, flag;

int main()
{
	int t;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin >> t;
	for (int times = 1; times <= t; times++) {
		cin >> n;
		if (n <= 0) {
			printf("Case #%d: INSOMNIA\n", times);
			continue;
		}
		m = 0;
		flag = false;
		memset(d, 0, sizeof(d));
		while (!flag) {
			m += n;
			sprintf(s, "%d", m);
			for (int i = 0; i < strlen(s); i++)
				d[s[i] - '0'] = true;
			flag = true;
			for (int i = 0; i < 10; i++)
				if (d[i] == false) {
					flag = false;
					break;
				}
		}
		printf("Case #%d: %d\n", times, m);
	}
	return 0;
} 
