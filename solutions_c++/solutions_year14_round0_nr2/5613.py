#include<vector>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

int main() {
	int t, case_num=0;
	scanf("%d", &t);
	while (t--) {
		double x, c, f;
		double sum_cookies, sum_time, new_rate;

		sum_cookies = 0;
		sum_time = 0;
		new_rate = 2;

		case_num++;
		scanf("%lf %lf %lf", &c, &f, &x);

		while (sum_cookies < x)
		{
			/* if we have the cost of a farm */
			if (sum_cookies >= c)
			{
				/* check if waiting is better than buying a farm */
				double time_if_wait = (x-sum_cookies)/new_rate;
				double time_if_buyed = (x - (sum_cookies - c))/(new_rate+f);

				if ( time_if_wait < time_if_buyed)
				{
					sum_time += time_if_wait;
					break;
				}

				/* buy new farm */
				sum_cookies -= c;
				new_rate += f;
			}
			/* we don't have enough money to buy a farm, then wait! */
			/* Check if target can be met before we own the cost of a farm */
			else
			{
				double time_to_win = (x-sum_cookies)/new_rate;
				double time_to__buy_farm = (c - sum_cookies)/(new_rate);

				if ( time_to_win < time_to__buy_farm)
				{
					sum_time += time_to_win;
					break;
				}
				else
				{
					sum_time += time_to__buy_farm;
					sum_cookies = c;
				}

			}

		}

		printf("Case #%d: %.7lf\n", case_num, sum_time);
	}
	return 0;
}
