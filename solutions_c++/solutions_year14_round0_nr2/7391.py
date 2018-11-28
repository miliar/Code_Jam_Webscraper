#include <iostream>
#include <iomanip>

using namespace std ;

int main(int argc, char const *argv[])
{
	int n;
	double C, F, X;
	bool loop;
	double prev, sum;
	cin >> n;
	cout.precision(7);
	for(int k=1; k<=n; ++k)
	{
		cin >> C >> F >> X;
		loop = true;
		prev = X/2;
		sum = 0;
		for(int i = 1 ; loop ; ++i)
		{
			sum += C / (2 + (i - 1) * F) ;
			double pres = X / (2 + i * F) + sum ;
			if(prev < pres)
			{
				loop = false ;
				cout<< "Case #" << k << ": " << fixed << prev << endl ;
			}
			else
			{
				prev = pres ;
			}
		}		
	}

	return 0;
}