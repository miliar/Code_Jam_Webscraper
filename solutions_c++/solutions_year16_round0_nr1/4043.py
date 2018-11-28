//Google Code Jam 2016
//Qualifier Round - Counting Sheep
//Tejal Singh

#include <iostream>
//#include <math>
using namespace std;
int main()
{
	int t;
	cin>>t;
	long long num;
	for(int i=0;i<t;i++)
	{
		cin>>num;
		if(num==0)
		{	
			cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
		}
		else
		{
			int arr[10];
			for(int j=0;j<10;j++)
			{
				arr[j]=0;
			}
			int count=0;
			int m=1;
			int dig;
			while(count!=10)
			{
				long long temp=num*m;
				while(temp!=0)
				{
					dig=temp%10;
					if(arr[dig]==0)
					{
						arr[dig]=1;
						count++;
					}
					temp=temp/10;
				}
				m++;
			}
			cout<<"Case #"<<i+1<<": "<<num*(m-1)<<endl;
		}
		
	}	
}
