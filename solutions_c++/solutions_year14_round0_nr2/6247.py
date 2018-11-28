#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ofstream output("ans.txt");
	int test_cases, cur_case;
	cin >> test_cases;

	for (cur_case = 1; cur_case <= test_cases; cur_case++) {
		double C, F, X;
		cin >> C >> F >> X;

		double gain_rate = 2.0;
		double gain_cookies = 0.0;
		double time_used = 0.0;

		while (gain_cookies < X) {
			if ((gain_cookies + C) >= X) {
				time_used += (X - gain_cookies) / gain_rate;
				break;
			}

			time_used += ((C - gain_cookies) / gain_rate);
			gain_cookies = C;

			double buy_time = (X - (gain_cookies - C)) / (gain_rate + F);
			double not_buy_time = (X - gain_cookies) / gain_rate;
			if (not_buy_time > buy_time) {
				gain_cookies -= C;
				gain_rate += F;
			}
			else {
				time_used += not_buy_time;
				break;
			}
		}
		//output << "Case #" << cur_case << ": " << ans << endl;
		output.precision(7);
		cout.precision(7);
		output << fixed << "Case #" << cur_case << ": " << time_used << endl;
		cout << fixed << "Case #" << cur_case << ": " << time_used << endl;

	}
}