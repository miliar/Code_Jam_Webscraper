#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
	int T;
	double C,F,X;
	double costWith, costWithOut;
	cin>>T;
	double total;
	
	double CPS = 2.0; //cost per second
	double initTime;

	for (int t = 1; t <= T; t++)
	{
		// Data input + initializing
		cin >> C >> F >> X;
		CPS = 2.0;
		double time = 0.0;
		costWithOut = X/CPS;
		costWith = C/CPS + X/(CPS+F);
		
		while (costWith < costWithOut)
		{
			time = time + C/CPS;
			CPS = CPS + F;
			costWithOut = X/CPS;
			costWith = C/CPS + X/(CPS+F);
		}
		
		time = time + X/CPS;

		cout<<setiosflags(ios::fixed)<<setprecision(7)<< time <<" "<<endl;
	}
}