/* Cookie */
#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	int T, i;
	double C, F, X, currentF, sum, first, second;
	cin >> T;
	for(i = 1; i <= T; i++)
	{
		cin >> C >> F >> X;
		sum = 0.0;
		currentF = 2.0;
		
		while(1)
		{
			first = X/currentF;
			second = (C/currentF)+(X/(currentF+F));
			
			if(second <= first)
			{
				sum += C/currentF;
				currentF += F;
			}
			else
			{
				sum += first;
				break;
			}
			
		}
		printf("Case #%d: %.7f\n", i, sum);
	}
	return 0;
}
