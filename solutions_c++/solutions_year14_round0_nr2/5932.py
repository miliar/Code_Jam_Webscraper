#include<iostream>
#include<fstream>

using namespace std;

int t;
double C,F,X,sum,current,next,rate;

int main()
{
	scanf("%d",&t);
	for(int tc=1;tc<=t;tc++)
	{
		
		current=next=sum=0.0;
		rate = 2.0;
		cin>>C>>F>>X;
		
		//printf("%f",C);
		
		do
		{
			next = sum+(C/rate)+(X/(rate+F));
			current = sum+(X/rate);
			sum += C/rate;
			rate+=F;
			
			
		}while(next < current);
		
			printf("Case #%d: %0.7f\n",tc,current);
	}
return 0;
}