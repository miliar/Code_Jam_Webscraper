#include <iostream>
using namespace std;

int main()
{
	int nCase = 0;
	double C, F, X;
	cin >> nCase;
	for (int i=0; i<nCase; i++)
	{
		cin >> C >> F >> X;
		
		bool bFind = false;
		int n = 0;
		while (!bFind)
		{
			double a = C / (2+n*F);
			double b = X/(2+n*F) - X/(2+(n+1)*F);

			if (a > b)
			{
				break;
			}

			n++;
		}

		double totalTime = 0;
		for (int j=0; j<n; j++)
		{
			totalTime += C/(2+j*F);
		}
		totalTime += X/(2+n*F);


		printf("Case #%d: %.7lf\n", i+1, totalTime);
	}			
	return 0;
}