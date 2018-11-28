#include <iostream>
#include <cstdio>
using namespace std;

int digits[10];
int counter;
void divide(long long int num)
{
	while(num)
	{
		int digit=num%10;
		if(digits[digit]==0)
		{
			digits[digit]=1;
			counter++;
		}
		num=num/10;
	}
}
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int T;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		for(int j=0;j<10;j++)
			digits[j]=0;
		counter=0;
		long long int num;
		cin>>num;
		if(num==0)
		{
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
			continue;
		}
		for(int j=1;j<1000000;j++)
		{
			divide(j*num);
			if(counter==10)
			{
				cout<<"Case #"<<i<<": "<<j*num<<endl;
				break;
			}
		}
	}
}