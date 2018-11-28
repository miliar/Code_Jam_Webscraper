#include <bits/stdc++.h>
using namespace std;
int N, num;
bool comprtr(int a, int b) {return a > b;}

int main() {
	freopen("B-small-attempt2.in","r",stdin);
    freopen("b3_new_ans.txt","w",stdout);
	int t,res;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
		{
		scanf("%d", &N);
		vector<int> vv, vv2;
		res = 0;
		for (int i = 0; i < N; i++) {
			scanf("%d", &num);
			res = max(res, num);
			vv.push_back(num);
			vv2.push_back(num);
		}

		int tm = 0;
		while (1)
		{
			if (vv.size() == 0)
				break;
			sort(vv.begin(), vv.end(), comprtr);
			int cur = vv[0];
			int tt = tm + cur;
			res = min(res, tt);
			if (cur <= 3)
				break;
			if (cur == 6)
			{
				vv[0] = 3;
				vv.push_back(3);
			}
			else if (cur == 9)
			{
				vv[0] = 3;
				vv.push_back(6);
			} else if (cur % 2 == 0) {
				vv[0] = cur / 2;
				vv.push_back(cur / 2);
			} else {
				vv[0] = cur / 2 + 1;
				vv.push_back(cur / 2);
			}
			tm++;
		}

		tm = 0;
		while (1) {
			if (vv2.size() == 0) break;
			sort(vv2.begin(), vv2.end(), comprtr);
			int cur = vv2[0];
			int tt = tm + cur;
			res = min(res, tt);
			if (cur <= 3)
				break;
			if (cur % 2 == 0) {
				vv2[0] = cur / 2;
				vv2.push_back(cur / 2);
			} else {
				vv2[0] = cur / 2 + 1;
				vv2.push_back(cur / 2);
			}
			tm++;
		}

		printf("Case #%d: %d\n", tt, res);
	}
	return 0;
}
