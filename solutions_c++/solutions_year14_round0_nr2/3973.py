#include<iostream>
#include<stdio.h>

using namespace std;

int main()
{
	int no_of_tests;
	double c[100],f[100],x[100];

	cin>>no_of_tests;
	for(int i = 0; i < no_of_tests; i++)
	{
		cin>>c[i]>>f[i]>>x[i];
		
		bool inc = false;
		int count = 0;
		double time = x[i]/2.0;
		double prev_time = x[i]/2.0;
		int n = 1;
		while(prev_time >= time)
		{
			prev_time = time;
			time = 0;
			for(int j = 0; j < n; j++)
				time += c[i]/(2.0 + (double)j * f[i]);
			time += x[i]/(2.0 + (double)n * f[i]);
			n++;
		}	
		
		//cout<<"Count: "<<count<<'\n';	
		printf("Case #%d: %f\n", i+1, prev_time);
	}

	return 0;
}
