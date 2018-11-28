#include <iostream>
#include <stdio.h>
#include <iomanip>

using namespace std;

int main ()
{
	int T = 0;
	int i = 0;
	double C = 0.0, F = 0.0, X = 0.0;
	double dt = 0.0, time = 0.0;
	
	cin >> T;
	
	for (int t = 0; t < T; t ++)
	{
		time = 0.0;
		
		cin >> C >> F >> X;
		
		i = 0;
		do
		{
			i ++;
			dt = X / (2 + i*F) + (C-X) / (2 + (i-1)*F);
			
		} while ( dt < 0.0 );

		for (int j = 1; j < i; j ++)
			time += C / (2 + (i-1-j)*F);
		time += X / (2 + (i-1)*F);

		cout << fixed << setprecision(7) << "Case #" << t+1 << ": " << time << endl;
	}
	
	return 0;
}
