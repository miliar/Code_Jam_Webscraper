#include <cstdio>
#include <queue>
#include <algorithm>
#include <memory.h>

using namespace std;

int main() {

	int T;
	scanf("%d",&T);
	for (int tc = 1; tc <= T; tc++) {
		int n,p;
		vector<int> pancake;
		for (int i = 0; i < 1005; i++)
			pancake.push_back(0);

		scanf("%d",&n);
		for (int i = 0; i < n; i++) {
			scanf("%d",&p);
			pancake[p]++;
		}

		queue<pair<vector<int>,int> > q;

		q.push(make_pair(pancake,0));

		while (!q.empty()) {
			vector<int> now = q.front().first;
			int k = q.front().second;
			q.pop();

			int sum = 0;
			for (int i = 1; i <= 1000; i++) {
				sum += now[i];
			}

			if (sum == 0) {
				printf("Case #%d: %d\n",tc, k);
				break;
			}

			vector<int> temp;

			for (int i = 1; i <= 1000; i++)
				temp.push_back(now[i]);
			temp.push_back(0);

			q.push(make_pair(temp,k+1));

			for (int i = 1000; i > 0; i--)
				if (now[i]) {
					int mid = i/2;
					vector<int> temp;
					for (int j = 2; j <= mid; j++) {
						temp = now;
						temp[j]++;
						temp[i-j]++;
						temp[i]--;
						q.push(make_pair(temp,k+1));
					}
					
					break;
				}
		}
	}
	return 0;
}