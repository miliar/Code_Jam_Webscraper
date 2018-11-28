#include <cstdio>
#include <algorithm>
#include <string>
#include <iostream>
#include <vector>
#include <cmath>
#include <queue>
using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);

	for (int TestCase = 1; TestCase <= T; TestCase++) {
		int N;
		scanf("%d", &N);
		priority_queue<pair<int, int> > q;

		int total = 0;
		for (int i = 0; i < N; i++) {
			int T;
			scanf("%d", &T);

			q.push(make_pair(T, i));

			total += T;
		}

		printf("Case #%d: ", TestCase);

		while(!q.empty()) {
			int now = q.top().first;
			int nowI = q.top().second;

			q.pop();

			if ((now - 1) * 2 > (total - 1)) {
				printf("%c%c ", nowI + 'A', nowI + 'A');
				total -= 2;
				
			}
			else if (q.top().first * 2 > (total - 1)) {
				int tmp = q.top().first;
				int tmpI = q.top().second;
				printf("%c%c ", nowI + 'A', tmpI + 'A');
				q.pop();

				total -= 2;
				if (tmp != 1)
					q.push(make_pair(tmp - 1, tmpI));
			}
			else {
				total--;
				printf("%c ", nowI + 'A');
			}
			if (now != 1)
				q.push(make_pair(now - 1, nowI));
		}
		printf("\n");
	}


	return 0;
}