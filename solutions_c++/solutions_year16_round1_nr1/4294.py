#include <cstdio>
#include <cstring>

char str[1005], buf[1005], buf2[1005];

void sol() {
	scanf("%s", str);
	int l = strlen(str), c = 0, c2 = 0;
	char t = str[0];
	for(int i = 1;i < l;i++) {
		if(str[i] >= t) {
			t = str[i];
			buf[c++] = str[i];
		}
		else buf2[c2++] = str[i];
	}
	for(int i = c - 1;i >= 0;i--) putchar(buf[i]);
	putchar(str[0]);
	for(int i = 0;i < c2;i++) putchar(buf2[i]);
	putchar(10);
}

int main() {
	int t;
	scanf("%d", &t);
	for(int ks = 1;ks <= t;ks++)
		printf("Case #%d: ", ks), sol();
}
