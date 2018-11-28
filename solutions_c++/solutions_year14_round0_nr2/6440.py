#include <iostream>
#include <iomanip>
#include<cstdio>
using namespace std;
int main()
{	
	int T;
	cin >> T;
	for(int i = 0; i < T; i++)
	{
		double C, F, X;
		cin >> C >> F >> X;
		double rate = 2.0;
		double prevT = X / rate;
		double prevA = 0.0;
		double currA;
		double currT;		
		while(true)
		{			
			currA = prevA + C / rate;
			rate += F;
			currT = currA + X / rate;
			if(currT > prevT)
				break;
			prevA = currA;
			prevT = currT;
		}
		cout << "Case #" << i+1 << ": ";
		printf("%.7lf\n", prevT);
	}
}