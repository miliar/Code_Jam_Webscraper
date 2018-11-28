#include <iostream>

using namespace std;

int try2(int a[])
{
	int flag=1;
	for(int i=0;i<10;i++)
	{
		if(a[i]==0)
		{
			return 0;
		}
		
	}
		if(flag==1)
		return 1;
}

int main()
{
	
	int n,i;
	cin>>n;
	int case1[10]={0};
	int *test=new int[n];
	for(i=0;i<n;i++)
		cin>>test[i];
	int temp,temp2,j,temp1;
	for(i=0;i<n;i++)
	{
		int case1[10]={0};	
		j=0;
		temp=test[i];
		temp1=temp;
		if(test[i]==0)
		cout<<"case #"<<i+1<<": "<<"INSOMNIA"<<endl;
		else
		{
		
		while(try2(case1)!=1)
		{
			
		
			while(temp!=0)
			{
				temp2=temp%10;
				case1[temp2]=1;
				temp/=10;
			}
			temp1+=test[i];
			temp=temp1;
			
		
		}
		temp-=test[i];
		
		cout<<"case #"<<i+1<<": "<<temp<<endl;
		
	}
	}
	
	
	
	
	return 0;
}
