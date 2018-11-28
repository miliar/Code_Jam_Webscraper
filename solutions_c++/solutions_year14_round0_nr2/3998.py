#include <iostream>
#include <cstdlib>
#include <cmath>
#include <iomanip>
#include <algorithm>
#include <string>


#define forn(i,n) for(int i = 0; i < (int)(n); i++)
#define forn1(i,n) for(int i = 1; i <= (int)(n); i++)
#define dforn(i,n) for(int i = (int)(n-1); i >= 0; i--)


using namespace std;

int main()
{
	cout.precision(7);
	cout.setf(ios::fixed | ios::showpoint);

	int test;
	double c, f, x;
	double sum, result;
	int lim;
	
	cin >> test;

	forn(t,test)
	{
		cin >> c >> f >> x;
		sum = 0.0;
		lim = (int) ( (x / c) - (2.0 / f) );
		
		lim = max(lim,0);

		//cout << lim << endl;		

		dforn(i,lim){
			sum += ( 1 / (2 + i * f) );
		}

		result = c * sum + x / (2 + lim*f);

		cout << "Case #" << (t+1) << ": " << result << endl;
	}
	
	return 0;
}
