#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <utility>
using namespace std;
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int k = 1; k <= t; k++)
	{
		char s[102] = { 0 };
		scanf("%s", &s);
		int cnt = 0;
		int len = strlen(s);
		

		for (int i = len - 1; i >= 0; i--) {

			if (s[i] == '-') {
				if (s[0] == '+') {
					int id = 0;
					while (true) {
						if (s[id] == '+') s[id] = '-';
						else break;
						id++;
					}
					//s[0] = '-';
					cnt++;
				}
				for (int j = 0; j <= i / 2; j++) {
					swap(s[j], s[i - j]);
				}
				for (int j = 0; j <= i; j++) {
					if (s[j] == '+') s[j] = '-';
					else s[j] = '+';
				}
				cnt++;
			}//바꿉니다 자리를
			//printf("/%s/", s);
		}

		printf("Case #%d: %d\n", k, cnt);
	}
	return 0;
}