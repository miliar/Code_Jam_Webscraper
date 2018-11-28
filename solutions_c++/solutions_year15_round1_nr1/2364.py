#include <stdio.h>
#include <stdlib.h>
#include <vector>
using namespace std;

int main() {
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("A-small-attempt0.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t;
	scanf("%d", &t);
	int n;
	vector<int> num;
	int tmp;
	int cur;
	int res1;
	int res2;
	int rate;
	int tmpRate;
	for (int tt = 1; tt <= t; tt++) {
		scanf("%d", &n); 
		num.clear();
		res1 = 0; 
		res2 = 0;
		tmpRate = 0;
		rate = 0;
		for (int i = 0; i < n; i++) {
			scanf("%d", &tmp);
			num.push_back(tmp);
		}

		cur = num[0];
		for (int i = 1; i < n; i++) {
			if (num[i] < cur) {
				tmpRate = cur - num[i];
				res1 += tmpRate;
				rate = max(rate, tmpRate);
				
			}
			cur = num[i];
		}
		for (int i = 0; i < n - 1; i++) {
			if (num[i] < rate) {
				res2 += num[i];
			} else {
				res2 += rate;
			}
		}
		printf("Case #%d: %d %d\n", tt, res1, res2);
	}
	return 0;
}