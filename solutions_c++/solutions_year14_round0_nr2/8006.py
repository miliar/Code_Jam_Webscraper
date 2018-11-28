#include<iostream>
#include<stdio.h>
#include<math.h>
#include<vector>
#include <stdlib.h>
#include <stack>
using namespace std;


int main()
{

	int t,var=0;

		cin>>t;

	while(t--)
	{
			double c,f,x,one, two,curr=2;
		double time=0;
		cin>>c>>f>>x;
	while(1)
	{

		one= x/curr;
		two=(c/curr)+x/(curr+f);
		if(one >two)
		{
			time+= c/curr;

		}

		else
		{

		time+=x/curr;
		break;
		}
		curr= curr+f;
	}
	cout<<"Case #"<<++var<<":"<<" ";
	printf("%.7f\n",time);

	}
}
