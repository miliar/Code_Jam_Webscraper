#include <bits/stdc++.h>
using namespace std;

bool isZero(double v)
{
	return std::abs(v)<1e-6;
}

void test()
{
	size_t N;
	double V, X;
	cin >> N >> V >> X;
	
	double low_rate=0, low_energy=0, high_rate=0, high_energy=0;
	double prop_rate=0;
	for (size_t i=0; i<N; ++i)
	{
		double rate, temp;
		cin >> rate >> temp;
		if (isZero(temp-X))
		{
			prop_rate += rate;
		}
		else if (temp < X)
		{
			low_rate += rate;
			low_energy += rate*temp;
		}
		else
		{
			high_rate += rate;
			high_energy += rate*temp;
		}
	}
	
	double low_temp = low_energy/low_rate;
	double high_temp = high_energy/high_rate;
	
	double time_high = (V*(X-low_temp))/(high_rate*(high_temp-low_temp));
	double time_low = (V*(X-high_temp))/(low_rate*(low_temp-high_temp));
	
	if (::isnan(low_temp) || ::isnan(high_temp))
		{}//cout << "IMPOSSIBLE";
	else if (isZero(high_temp-low_temp))
		{}//cout << V/(low_rate+high_rate);
	else
		//cout << setprecision(12) << std::max(time_high, time_low);
		prop_rate += V/std::max(time_high, time_low);
		
	cout.setf(ios::fixed);
	if (isZero(prop_rate))
		cout << "IMPOSSIBLE";
	else
		cout << setprecision(10) << V/prop_rate;
}

int main()
{
	size_t c;
	cin >> c;
	for (size_t i = 1; i<=c; ++i)
	{
		cout << "Case #" << i << ": ";
		test();
		cout << endl;
	}
}
