#include <iostream>
#include <iomanip>
#include <cassert>
#include <cmath>

using namespace std;

void doCase()
{
	int N;
	double V, X;
	
	cin >> N >> V >> X;
	
	if (N == 1)
	{
		double R1, C1;
		cin >> R1 >> C1;
		if (abs(C1-X) > 0.00001)
		{
			cout << "IMPOSSIBLE" << endl;
		}
		else
		{
			cout << fixed;
			cout << setprecision(10);
			cout << V/R1 << endl;
		}
	}
	else
	{
		double R1, C1, R2, C2;
		cin >> R1 >> C1 >> R2 >> C2;
		
		if ((C1 > X+0.00001 && C2 > X+0.00001) || (C1 < X-0.00001 && C2 < X-0.0001))
		{
			cout << "IMPOSSIBLE" << endl;
		}
		else if (abs(C1 - C2) < 0.00001)
		{
			assert(abs(C1- X) < 0.00001);
			double R = R1 + R2;
			cout << fixed;
			cout << setprecision(10);
			cout << V/R << endl;
		}
		else
		{
			double V1 = V*(X-C2)/(C1-C2);
			double V2 = V*(X-C1)/(C2-C1);
			
			assert(abs(V1+V2-V) < 0.000001);
			assert(abs((C1*V1+C2*V2)/V-X) < 0.000001);

			double time = max(V1/R1, V2/R2);
			cout << fixed;
			cout << setprecision(10);
			cout << time << endl;
		}
	}
}

int main()
{
	int T;
	cin >> T;
	for (int i=0; i<T; i++)
	{
		cout << "Case #" << i+1 << ": ";
		doCase();
	}
	return 0;
}
