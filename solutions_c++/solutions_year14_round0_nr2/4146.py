#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

int main()
{
	int t,tcase;
	long double C,F,X;
	cin>>tcase;
	for(t=1; t<=tcase; t++)
	{
		cin>> C>> F>> X;
		double prevSum = 0,prevRes = 0;
		double currSum = 0,currRes = 0;
		int iter = -1;
		while(1)
		{
			if(iter>-1)
				currSum = prevSum + C/(2+iter*F);
			iter ++;
			currRes = currSum + X/(2+iter*F);
			if(currRes > prevRes && prevRes)
			{
				//cout<<iter<<endl;
				printf("Case #%d: %.7lf\n",t,prevRes);
				break;
			}
			prevSum = currSum;
			prevRes = currRes;
		}
	}
	return 0;
}
