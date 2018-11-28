#include<iostream>
#include<conio.h>
using namespace std;
int main()
{
	int test_cases;
	cin>>test_cases;
	int index=0;
	int smax,arr[1005],result[100];
	char str[1005];
	int counter,sum;
	for(int u=1;u<=test_cases;u++)
	{
		cin>>smax;
		cin>>str;
		for(int h=0;h<=smax;h++)
		{
			arr[h]=str[h]-48;
		}
	
	counter=0;
	sum=0;
	for(int g=0;g<=smax;g++)
	{
		if(counter>=g)
		counter=counter+arr[g];
		else
		{
			while(counter!=g)
			{
				++sum;
				++counter;
			}
			counter=counter+arr[g];
		}
	}
	result[index]=sum;
	++index;
}//end of for loop
	for(int q=0;q<100;q++)
	{
		cout<<"Case #"<<q+1<<": "<<result[q]<<"\n";
	}
	return 0;
}
