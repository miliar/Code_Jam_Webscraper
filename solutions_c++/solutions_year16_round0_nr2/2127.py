#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

int N, l;
char s[105];
bool now, goa;

int main(int argc, char** argv) {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	
	scanf("%d", &N);
	gets(s);
	
	for (int times = 1; times <= N; ++times) {
		printf("Case #%d: ", times);
		gets(s);
		l = strlen(s);
		goa = true;
		int ans = 0;
		
		for (int i = l-1; i >= 0; --i) {
			now = s[i] == '+';
			if (now != goa) {
				goa = !goa;
				ans ++;
			}
		}
		
		printf("%d\n", ans);
	}
	return 0;
}

