#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	double C,F,X;
	double total;
	double rate;
	double time1, time2;
	cin >> T;
	cout << fixed;
	cout.precision(7);
	for (int t=0; t<T; t++)
	{
		rate=2.0;
		total=0;
		cin >> C >> F >> X;
		if (X<C) {cout << "Case #" << t+1 << ": " << X/2.0 << endl; continue;}
		while (true)
		{
			time1 = C/rate + X/(rate+F);
			time2 = X/rate;
			if (time1<time2)
			{
				total+=C/rate;
				rate+=F;
			}
			else {
				total+=time2;
				break;
			}
		}
		cout << "Case #" << t+1 << ": "  << total << endl;
	}
	return 0;
}