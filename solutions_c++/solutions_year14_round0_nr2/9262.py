#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

int main()
{
	int test_cases;
	double cost, farm, score;
	cin >> test_cases;

	for(int test_c = 1; test_c <= test_cases; ++test_c)
	{
		cin >> cost >> farm >> score;
		vector<double> times;

		double click_rate = 2;

		while( score > (click_rate * score)/(click_rate + farm) + cost )
		{
			times.push_back(cost/click_rate);
			click_rate += farm;
		}
		times.push_back(score/click_rate);

		double total = 0;

		for(unsigned int i=0; i<times.size();++i)
		{
			total += times[i];
		}

		cout << "Case #" << test_c << ": "  << fixed << setprecision(7) << total << endl;
	}
}
