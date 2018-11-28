#include <iostream>
#include <stdio.h>
using namespace std;
int main()
{
	double C,F,X,coinRate,overHead,min_time,curr_time;
	int t,num = 1;
	cin>>t;
	while(t--)
	{
		cin>>C>>F>>X;
		coinRate = 2.0;
		overHead = 0.0;
		min_time = X/(double)2;
		while(X/(double)coinRate + overHead <= min_time)
		{
			curr_time = X/(double)coinRate + overHead;
			// cout<<overHead<<" "<<X/(double)coinRate<<endl;
			if(curr_time < min_time)
				min_time = curr_time;
			overHead += C/coinRate;
			coinRate += F; 
		}
		// cout<<"case #"<<num<<": "<<setprecision(6)<<min_time<<endl;
		printf("case #%d: %0.7F\n",num,min_time);
		num++;
	}
	return 0;
}