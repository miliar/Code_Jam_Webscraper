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

bool ck(big x, int &st) {
	while (x) {
		st |= 1 << (x % 10);
		x /= 10;
	}
	return (st + 1) == (1 << 10);
}

int main() {
	int i;
//	for (i = 1; i <= 1000000; i++) {
//		int j = 0;
//		int st = 0;
//		for (j = 1; j <= 1000; j++) {
//			if (ck(1ll * i * j, st))
//				break;
//		}
//		if (j > 1000)
//			cerr << "cannot: " << i << endl;
//	}
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int cas, cass;
	scanf("%d", &cas);
	for (cass = 1; cass <= cas; cass++) {
		int i, st = 0, n;
		scanf("%d", &n);
		printf("Case #%d: ", cass);
		if (!n) {
			printf("INSOMNIA\n");
			continue;
		}
		for (i = 1; i <= 1000; i++)
			if (ck(1ll * n * i, st))
				break;
		printf("%I64d\n", 1ll * i * n);
	}
	fclose(stdin);
	fclose(stdout);
}

