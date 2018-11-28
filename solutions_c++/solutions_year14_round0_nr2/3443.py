#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
	int T;
	cin >> T;
	long double C,F,X;
	for (int i= 1; i<= T;i++)
	{
		cin >> C >>F >> X;
		long double  ctime;
		long double temp_F = 2;
		bool proceed = true;
		long double sum = 0.0;
		while(proceed != false)
		{
			ctime = (long double)((C/temp_F)+ (X/(temp_F+F)));
			if ((X/temp_F) > ctime)
			{
				sum +=(long double) (C/temp_F);
				temp_F +=(long double) F;
			}
			else
			{
				sum += (long double)(X/temp_F);
				proceed = false;
			}	
		}
		cout << "Case #"<<i<<": "<<fixed << setprecision(7) << sum << endl;
	}
	return 0;
}
