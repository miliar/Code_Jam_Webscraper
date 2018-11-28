//author: whd

#pragma comment(linker, "/STACK:1024000000,1024000000")
#include <iostream>
#include <string>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <queue>
#include <set>
#include <map>

#define mp make_pair
#define pb push_back
#define x first
#define y second

using namespace std;
typedef long long big;

typedef pair<int, int> pii;

char str[2000];
int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int cas, cass;
	scanf("%d", &cas);
	for (cass = 1; cass <= cas; cass++) {
		printf("Case #%d: ", cass);
		scanf("%s", str + 1);
		int i, last, cnt = 0;
		for (i = 1; str[i]; i++) {
			if (str[i] != str[i - 1]) {
				cnt++;
			}
			last = str[i] == '+';
		}
		printf("%d\n", cnt - last);
	}
	fclose(stdin);
	fclose(stdout);
}

