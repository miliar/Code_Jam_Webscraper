#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	int T;
	cin>>T;

	double C,F,X;
	cout << fixed << setprecision(7);
	
	for(int i=0; i<T; ++i)
	{
		cin>>C>>F>>X;

		double rate = 2.0;
		double t = 0;
		double cookie = 0.0;

		double farm_time;

		while(true) {

			farm_time = C/rate;

			if (X/rate > (farm_time + X/(rate + F))) {
				t += farm_time;
				rate += F;
			}
			else
				break;

		}

		t += X/rate;

		cout<<"Case #"<<i+1<<": "<<t<<endl;

	}
}
