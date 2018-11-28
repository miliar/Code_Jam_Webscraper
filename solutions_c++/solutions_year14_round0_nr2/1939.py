#include<cstdio>
#include<iostream>
#include<iomanip>

using namespace std;

int main()
{

	int t, T;

	cin>>T;
	for(t=1;t<=T;t++)
	{

		long double C, F, X;
		long double curr=2, max, time =0;
	
		cin>>C>>F>>X;

		max = (F * X)/ C - F;

		while(curr<max)
		{
			time += (C/curr);
			curr+=F;
		
			
		}
		
		time+=(X/curr);

		
	    	std::cout << std::fixed;
		std::cout << std::setprecision(7);
		cout<<"Case #"<<t<<": "<<time<<endl;

	}

	return 0;
}
