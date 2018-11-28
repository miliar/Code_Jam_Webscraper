#include <stdio.h>
#include <stdlib.h>
#include <queue>
#include <algorithm>

class Dish {
public:
	int pre;
	int cur;
	int div;

	Dish(int p) {
		pre = cur = p;
		div = 1;
	}
	bool operator<(const Dish& other) const {
		return cur < other.cur;
	}
};

int main()
{
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		std::priority_queue<Dish> q;
		int D;
		scanf("%d", &D);
		for (int i=0; i<D; i++) {
			int a;
			scanf("%d", &a);
			q.push(Dish(a));
		}
		int res = q.top().cur;
		int spe = 0;
		while (spe < res) {
			Dish first = q.top();
			q.pop();
			first.div++;
			first.cur = (first.pre - 1) / first.div + 1;
			q.push(first);
			spe++;
			res = std::min(res, q.top().cur + spe);
		}
		printf("Case #%d: %d\n", t, res);
	}
}
