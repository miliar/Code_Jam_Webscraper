#include<cstdio>
using namespace std;

int main()
{
	freopen("D:\\B-small-attempt0.in", "r", stdin);
	freopen("D:\\B-small-attempt0.out", "w", stdout);
	int T, TT;
	scanf("%d", &T);
	TT = T;
	while (T--){
		double c, f, x;
		scanf("%lf%lf%lf", &c, &f, &x);
		double lastCost=1000000000;
		double minCost=1000000000;
		for (int i = 0; i < 50002; i++){
			double cost = 0;
			double speed = 2;
			for (int j = 0; j < i; j++){
				double needTime = c / speed;
				cost += needTime;
				speed += f;
				if (cost>minCost)
					break;
			}
			cost += x / speed;
			if (cost<minCost)
				minCost = cost;
		}
		printf("Case #%d: %.7lf\n",TT-T, minCost);
	}
	return 0;
}