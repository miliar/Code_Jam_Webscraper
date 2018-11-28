#include <iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;
	cout.setf( std::ios::fixed, std:: ios::floatfield );
	cout.precision(7);
	for(int num=1; num<=T; num++)
	{
		double C, F, X;
		cin >> C >> F >> X;
		double p = 2;
		double t = 0;
		double c = 0;
		bool finished = false;
		while(!finished)
		{
			double toFarm = (C-c)/p;
			if((X-c)/p < toFarm+X/(p+F))
			{
				t += (X-c)/p;
				finished = true;
			}
			else
			{
				t += toFarm;
				p += F;
			}
		}
		cout << "Case #" << num << ": " << t << endl;
	}
	return 0;
}
