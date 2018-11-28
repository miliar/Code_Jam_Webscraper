#include <iostream>
#include <vector>
using namespace std;

int main()
{
	cout.precision(20);

	int T;
	cin >> T;


	for(int t = 1; t <= T; ++t)
	{
		double c, f, x;
		cin >> c >> f >> x;

		if(c >= x)
		{
			cout << "Case #" << t << ": " << x/2 << endl;
			continue;
		}

		double minRate = f/c*(x-c);

		double rate = 2;
		double time = 0;
		while(rate < minRate)
		{
			time += c/rate;
			rate += f;
		}

		time += x/rate;

		cout << "Case #" << t << ": " << time << endl;
	}
}
