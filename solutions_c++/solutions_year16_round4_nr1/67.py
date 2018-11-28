#include <cstdio>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <algorithm>

using namespace std;

const int N = 13;
int c[N][3];

void init() {
	c[0][0] = 1;
	c[0][1] = 0;
	c[0][2] = 0;
	for (int n = 1; n <= N; n++) {
		c[n][0] = c[n - 1][0] + c[n - 1][2];
		c[n][1] = c[n - 1][1] + c[n - 1][0];
		c[n][2] = c[n - 1][2] + c[n - 1][1];
	}
}

const char *str="RSP";
char buf[(1 << N) + 5], tmp[1 << N];
int ptr;
void print(int n, int id) {
	if (n == 0) {
		buf[ptr++] = str[id%3];
	} else {
		char *s = buf + ptr;
		print(n - 1, id);
		print(n - 1, id + 1);
		int l = 1 << (n - 1);
		if (strncmp(s, s + l, l) > 0) {
			memcpy(tmp, s, l);
			memcpy(s, s+l, l);
			memcpy(s+l, tmp, l);
		}
	}
}

void run(int cas) {
	int n, r, p, s;
	scanf("%d%d%d%d", &n, &r, &p, &s);
	printf("Case #%d: ", cas);
	ptr = 0;
	bool f = true;
	if (c[n][0] == r && c[n][1] == s && c[n][2] == p)
		print(n, 0);
	else if (c[n][0] == s && c[n][1] == p && c[n][2] == r)
		print(n, 1);
	else if (c[n][0] == p && c[n][1] == r && c[n][2] == s)
		print(n, 2);
	else f = false;
	buf[ptr] = 0;
	if (f)
		printf("%s\n", buf);
	else
		printf("IMPOSSIBLE\n");
}

int main() {
	init();
    int tt, cas;
    scanf("%d", &tt);
    for (cas = 1; cas <= tt; cas++)
        run(cas);
    return 0;
}

