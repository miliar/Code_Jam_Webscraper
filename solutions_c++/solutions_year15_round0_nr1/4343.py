#include <cstdio>

int main() {
	int t;
	scanf("%d",&t);
	for (int t1 = 1; t1 <= t; t1++) {
		int smax;
		scanf("%d",&smax);
		char *s = new char[smax+1];
		for (int i = 0; i <= smax; i++) {
			char a;
			scanf("%c",&a);
			if (a < '0' || a > '9')
				i--;
			else
				s[i]=a-'0';
		}
		int add = 0;
		int standing = 0;
		for (int i = 0; i <= smax; i++) {
			if (standing >= i)
				standing += s[i];
			else if (s[i] != 0) {
				add += i-standing;
				standing = i + s[i];
			}
		}
		printf("Case #%d: %d\n", t1, add);
		delete[] s;
	}
}
