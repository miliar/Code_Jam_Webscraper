#include <algorithm>
#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;
	
int main()
{
	double c, f, x;
	int t;
	cin >> t;
	vector <double> sum (100000), psum (100000);
	for (int i = 0; i < t; ++i)
	{
		cin >> c >> f >> x;
		sum[0] = x/2, psum[0] = 0.;
		
		int j = 1;
		for (;; ++j)
		{
			psum[j] = psum[j-1] + c / (2 + (j-1)*f);
			sum[j] = psum[j] + (x / (2 + j*f));
			if (sum[j] > sum[j-1])
				break;
		}
		
		cout << "Case #" << i+1 << ": " << fixed << setprecision (7) << min (sum[0], sum[j-1]) << endl;
	}
	return 0;
}