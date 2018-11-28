
#include <cstdio>
#include <iostream>

using namespace std;

int T;
double C, F, X;

double minTime()
{
	double rate = 2, time = 0;
	bool flag;
	
	do
	{
		double stay = X / rate;
		double buy = ( C / rate ) + ( X / (rate + F) );
		
		flag = (stay < buy) ? true : false;
		
		if(flag) {
			time += stay;
		}
		else 
		{
			time += ( C / rate );
			rate += F;
		}
	} while(!flag);
	
	return time;
}

int main()
{
	freopen("cookie.in", "r", stdin);
	freopen("cookie.out", "w", stdout);
	
	cin >> T;
	
	for(int x = 0; x < T; x++)
	{
		cin >> C >> F >> X;
		printf("Case #%d: %0.7f\n", x+1, minTime() );
	}
	
	return 0;
}

