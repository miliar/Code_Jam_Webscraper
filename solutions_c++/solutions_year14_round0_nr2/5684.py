#include <iostream>
#include <vector>
#include <stdio.h>

using namespace std;

int main() {
	vector<long double> time_passed;
	int cases, idx;
	const long double base_f = 2;
	long double cur_f, c, f, x;
	long double time_passed_one, time1, time2, total_time;


	cin >> cases;
	for (idx = 1; idx <= cases; idx++) {
		//cin >> c >> f >> x;
		scanf("%Lf %Lf %Lf", &c, &f, &x);
		cur_f = base_f;
		time_passed_one = 0;
		total_time = 0;
		while (1) {
			total_time = 0;
			for (vector<long double>:: iterator iter = time_passed.begin(); iter != time_passed.end(); ++iter)
				total_time += *iter;
			time1 = x / cur_f;
			time2 = c / cur_f + x / (cur_f + f);
			if (time1 < time2)
				break;
			time_passed_one = c / cur_f;
			time_passed.push_back(time_passed_one);
			cur_f += f;
		}

		total_time += x / cur_f;

		//cout << "Case #" << idx << ": " << total_time << endl;
		printf("Case #%d: %.7Lf\n", idx, total_time);
		time_passed.clear();
	}
}
