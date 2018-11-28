#include <iostream>
#include <iomanip>
#include <math.h>  
#include <stdio.h>

using namespace std;

int main()
{
	int T;
	cin >> T;
	double C, F, X, Fi = 0, tau = 0;
	cout.precision(7);	
	for( int i = 1; i <= T; i++ )
	{
		//int C, F, X, Fi = 0, tau = 0;
		cin >> C >> F >> X;
		Fi = 2;
		tau = 0;
		if( C*(Fi+F) < X*F )
		{
		double k = (double)(X*F-C*Fi)/(C*F) - 1;
		k = ceil(k);
		//cout <<  "" << k << endl;
		
		for( int j = 0; j < k; j++ )
			tau += (double)C/(Fi+j*F);
		
		tau += (double)X/(Fi+k*F);
		cout << fixed;
		cout << "Case #" << i << ": " << tau << endl;
		}
		else
		{
			//printf("%.6g\n", (double)X/Fi);
			tau = X/Fi;
			cout << fixed;
			cout << "Case #" << i << ": " << tau << endl;
		}
		//int temp = 0;
		/*while( X != 0 )
		{
			Fi = F;
			if( C*(Fi + F) < X*F )
			{
				tau += C/Fi;
				Fi += F;
			}
			else
			{
				tau += X/Fi;
				X = 0;
			}
		}
		cout << tau << endl;
		*/
	}
	return 0;
}
