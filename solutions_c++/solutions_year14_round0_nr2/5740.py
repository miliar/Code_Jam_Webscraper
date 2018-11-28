#include <stdio.h>
#include <iostream>

using namespace std;

int main()
{
	int t;
	cin>>t;

	for(int i=1;i<=t;i++)
	{
		double n = 2.00000;
		double c,f,x;
		cin>>c>>f>>x;

		double answer = 0.000000;
		double coins = 0.000000;

		while(coins<x)
		{
			coins = c;
			answer+= c/n;
			
			if((x-c)/n > x/(n+f))
			{
				coins = 0;
				n+=f;				
			}	

			else
			{
				coins = x;
				answer += (x-c)/n;
			}	
		}	

		printf("Case #%d: %0.7f\n",i,answer);

	}	

}