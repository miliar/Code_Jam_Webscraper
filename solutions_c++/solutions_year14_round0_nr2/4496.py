#include <iostream>
#include <algorithm>    // std::sort
#include <vector>       // std::vector
#include <fstream>
#include <limits>
#include <iomanip>
using namespace std;

int main()
{
	ofstream myfile;
	myfile.open ("cooko.txt");
	cout.precision(std::numeric_limits<double>::digits10);
	double	 test, c, f, x, rate, tim;
	cin >> test;
	for (int i = 0; i < test; ++i)
	{
		cin >> c >> f >> x;
		rate=2;
		tim=0;
		while(1){
			if (c/rate + (x)/(rate+f) < x/rate )
			{
				tim+=c/rate;
				rate+=f;
				// cout << "rate=" << rate << endl;
			}else{
				tim+=x/rate;
				break;
			}
		}
		
		myfile <<  setprecision(6)<<fixed<<"Case #" << i+1 << ": " << tim << endl;
	}
}