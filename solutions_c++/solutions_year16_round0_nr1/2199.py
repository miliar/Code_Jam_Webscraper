#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>

using namespace std;
bool used[20];
const int N = 1111111;
void check(long long x) {
	while (x) {
		used[x % 10] = true;
		x /= 10;
	}
}
int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int cas;
	scanf("%d", &cas);
	for (int cases = 1; cases <= cas; cases ++) {
		int n, i;
		scanf("%d", &n);
		memset(used, 0, sizeof used);
		for (i = 1; i < N; i++) {
			bool stop = true;
			long long t = (long long)n * i;
			check(t);
			for (int j = 0; j < 10; j++)
				if (used[j] == false)
					stop = false;
			if (stop)
						break;
		}
		printf("Case #%d: ", cases);
		if (i == N)
			printf("INSOMNIA\n");
		else
			cout << (long long)n * i << endl;
	}
}
