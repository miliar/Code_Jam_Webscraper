#include <iostream>
using namespace std;
int main(void)
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int n;
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		}
		else
		{
			int hash[10]={0};
			int k=1;
			int count=0;
			int temp,tt;
			while(count!=10)
			{
				temp=n*k;
				tt=temp;
				while(temp!=0)
				{
					if(!hash[temp%10])
						{
							count++;
							hash[temp%10]++;
						}
					temp=temp/10;
				}
				k++;
			}
			cout<<"Case #"<<i<<": "<<tt<<endl;
		}
	}
}