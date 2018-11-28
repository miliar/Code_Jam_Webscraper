#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
using namespace std;


int T;
int smax;
char str[1100];
int count;

int main() {

	freopen("C:\\Users\\wzh22014\\Downloads\\A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);

	scanf("%d", &T);

	count = 0;

	while (T--) {
		int cp = 0;
		int res = 0;
		count++;
		scanf("%d", &smax);
		scanf("%s", str);
		cp += str[0] - '0';
		for (int i = 1; i <= smax; i++) {
			if (str[i] == '0')
				continue;
			if (cp >= i) {
				cp += str[i] - '0';
			}
			else {
				res += i - cp;
				cp = i + str[i] - '0';
			}
		}
		printf("Case #%d: %d\n", count, res);
	}


}