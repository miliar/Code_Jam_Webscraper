#include <iostream>
#include <conio.h>
#include <string>
#include <string.h>
using namespace std;
bool checker();
int check[10]={0};
int f()
{
	int number;
	cin>>number;
	int temp2=number;
	int temp;
	if (number==0)
		return 0;
	for (int i=0;;i++)
	{
		temp=number;
		while(temp!=0)
		{
			check[temp%10]=1;
			temp=temp/10;
		}
		if (checker()==1)
		{
			for(int j=0;j<10;j++)
			{
				check[j]=0;
			}
			return number;
		}
		number+=temp2;
		
	}
}

bool checker()
{
	for(int j=0;j<10;j++)
	{
		if (check [j]==0)
		{
			return 0;
		}
	}
	return 1;//1 means all are 1
}
int main()
{
	int a;
	cin>>a;
	int out[a];
	for(int j=0;j<a;j++)
	{
		out[j]=f();
	}
	for (int i=0;i<a;i++)
	{
		cout<<"Case #"<<i+1<<": ";
		if(out[i]==0)
		cout<<"INSOMNIA"<<endl;
		else
		cout<<out[i]<<endl;
	}
	return 0;
}
