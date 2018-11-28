#include <iostream>
#include <stdio.h>
using namespace std;


int main()
{
	int T;
	cin >> T;
	for(int tt = 1; tt <= T; tt++)
	{
		double c, f, x;
		cin >> c >> f >> x;
		
		int n = 0;
		double t = 0, mt = x / 2.0;
		
		while (true)
		{
			t += c / ( n * f + 2);
			n += 1.0;
		
			double tn = t + x / ( n * f + 2);
			if (mt > tn)
			{
				mt = tn;
			}
			else
			{
				break;
			}
			
		}
		printf("Case #%d: %.7f\n", tt, mt);
	}
}
