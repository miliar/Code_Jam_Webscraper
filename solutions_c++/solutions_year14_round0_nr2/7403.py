#include <iostream>
#include <iomanip>
using namespace std;

typedef long double ld;
ld INF = 1e12;

int main()
{
	int num_cases;
	cin >> num_cases;
	for(int c = 0; c < num_cases; c++)
	{
		ld farm_cost, farm_rate, win_con, best = INF;
		ld acc_rate = 2, acc_time = 0;
		cin >> farm_cost >> farm_rate >> win_con;
		for(int n = 0; n <= win_con+1; n++)
		{
			best = min(best, acc_time + win_con/acc_rate);
			acc_time += farm_cost/acc_rate;
			acc_rate += farm_rate;
		}
		printf("Case #%d: %.7lf\n", c+1, (double)best);
	}
	return 0;
}
