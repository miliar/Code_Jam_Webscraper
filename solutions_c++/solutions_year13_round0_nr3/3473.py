#include "iostream"
#include "math.h"
using namespace std;

bool checkpalindromes(double);
void main()
{
	double yyy;
	int out=1;
	int exit;
	cin>>exit;
	char temp;
	double a,b,temp1;
	bool check;
	int SF;
	while(exit>0)
	{
		SF=0;
		exit--;
		cin>>a>>b;
		for(double i=a;i<=b;i++)
		{
			
			temp1=sqrt(i);
			
			if(modf(temp1,&yyy)==0)
			{
				check=checkpalindromes(i);
				if(check)
					if(checkpalindromes(temp1))
					SF++;
			}
					
		}
	cout<<"Case #"<<out<<": "<<SF<<endl;
	out++;

	}
}
bool checkpalindromes(double x)
{
	if(x<10)
		return true;
	else
	{
		int temp[14];
		int counter=0;
		while(x>=1)
		{
			
			temp[counter]=fmod(x,(double)10);
			counter++;
			x=x/10;
		}
		for(int i=0;i<counter/2;i++)
		{
			if(temp[i]!=temp[counter-i-1])
				return false;
		}
		return true;

	}
}
