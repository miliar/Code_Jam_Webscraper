#include<iostream>
using namespace std;
int main()
{
	int test,total;
	cin>>test;
	total=test;
	while(test--)
	{
		long int n,i=1,num,rem,j;
		cin>>n;
		int arr[10]={0};
		while(1)
		{
			if(n==0)
			{
				cout<<"Case #"<<total-test<<": INSOMNIA"<<endl;
				break;
			}
			for(j=0;j<10;j++)
			{
				if(arr[j]==0)
				break;
			}
			if(j==10)
			{
				cout<<"Case #"<<total-test<<": "<<n*(i-1)<<endl;
				break;
			}
			else
			{
				num=n*i;
				while(num>0)
				{
					rem=num%10;
					num/=10;
					arr[rem]=1;
				}
			}
			
			i++;
		}
	}
	
}
