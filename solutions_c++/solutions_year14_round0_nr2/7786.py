#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int c=1; c<=T; c++)
	{
		double C,F,X;
		double time=0;
		double min;
		double CookiesPerSec=2;
		
		cin >> C >> F >> X;

		min=X;


		int farm=0;

		while(1)
		{
			if(time + X/CookiesPerSec < min)
				min = time + X/CookiesPerSec;

			time+=C/CookiesPerSec;
			farm++;
			CookiesPerSec+=F;


			if(farm*C>=X)
				break;
		}



		printf("Case #%d: %.7f\n", c, min);
	}
}