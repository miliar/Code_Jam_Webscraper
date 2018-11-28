#include <stdio.h>
#include <iostream>
using namespace std;
 
int main() {
	// your code goes here
	int _T, idx;
	double C, F, X;
	double cookies = 0;
	idx = 0;
	cin >> _T;
	while(idx < _T)
	{
		double rate = 2.0000000f;
		double timecost = 0;
		bool finished = false;
		cin >> C >> F >> X;
		while(!finished)
		{
			double time1 = C / rate + X / (rate + F);
			double time2 = X / rate;
			if(time1 < time2)
			{
				timecost += C / rate;
				rate += F;
			}else
			{
				timecost += time2;
				finished = true;
			}
		}
		idx++;
		printf("Case #%d: %.7f\n", idx, timecost);
		// cout << "Case #" << idx << ": ";
		// cout << timecost << endl;
	}
	return 0;
}