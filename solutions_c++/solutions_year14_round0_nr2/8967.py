#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	int T;
	cin>>T;

	for (int i = 0; i < T; ++i)
	{
		double C,F,X;
		cin>>C>>F>>X;

		int farms = 0;
		while (1)
		{
			double rate = 2.0 + farms*F;
			double timeCurrent = X/rate;
			double timeNext = C/rate + X/(rate + F);

			if (timeCurrent < timeNext)
				break;
			++farms;
		}

		double t = 0;
		double rate = 2.0;
		for (int i = 0; i < farms; ++i)
		{
			t += C/rate;
			//cout<<t<<endl;
			rate += F;
		}

		t += X/rate;

		cout<<"Case #"<<i+1<<": "<<setprecision(7)<<fixed<<t<<endl;
	}
}