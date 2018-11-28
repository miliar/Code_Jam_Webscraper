//============================================================================
// Name        : prblm2_cookies.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int main()
{
	int t;
//	cout<<"Enter the total number of test cases:";
	cin>>t;
	double arr_ans[t];
	for(int z=0;z<t;z++)
	{
		double c,f,x,totaltime=0.0000000;
//		cout<<"Enter the farmcost:";
		cin>>c;
//		cout<<"Enter the farm production:";
		cin>>f;
//		cout<<"Enter the total requirement:";
		cin>>x;
		double r=2.0000000;
		while((x/r)>((x/(r+f))+c/r))
		{
			totaltime+=c/r;
			r+=f;

		}
		totaltime+=(x/r);
		arr_ans[z]=totaltime;
	}
	cout.setf(ios::showpoint);
	for(int z=0;z<t;z++)
	{
		int count=0;
		int k=arr_ans[z];
		while(k>=1)
		{
			k/=10;
			count++;
		}
		cout.precision(count+7);
		cout<<"Case #"<<z+1<<": "<<arr_ans[z]<<endl;
	}


	return 0;
}
