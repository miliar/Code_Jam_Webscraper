#include <cmath>
#include <cstdio>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <set>

using namespace std;

int main(){
#ifndef ONLINE_JUDGE
	freopen("/Users/malzantot/Documents/codingspace/input.in", "r", stdin);
	freopen("/Users/malzantot/Documents/codingspace/output2.txt", "w", stdout);
#endif
	int tt;
	scanf("%d", &tt);
	for (int ii = 1; ii<=tt; ii++) {
		printf("Case #%d: ", ii);
		int s_max;
		scanf("%d ", &s_max);
		int result = 0;
		int cur_shy = 1;
		int cur_count = getchar()-'0';
		while (cur_shy <= s_max) {

			int cnt = getchar() - '0';
			//printf("** cnt = %d\n", cnt);
			if (cur_count < cur_shy  && cnt > 0) {
				result += (cur_shy - cur_count);
				cur_count = cur_shy;
			}
		//	printf("+%d %d %d\n", result, cur_shy, cur_count);

			cur_count += cnt;
			cur_shy++;

		}
		printf("%d", result);
		puts("");
	}
	return 0;
}
