# include <iostream>
using namespace std;
int main()
{
	long t;
	cin>>t;
	for(long i=1;i<=t;i++)
	{
		long num;
		cin>>num;
		if(num==0)
		{
			cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		int arr[10]={0,0,0,0,0,0,0,0,0,0};
		long temp=num;
		int flag;
		for(int j=1;j>0;j++)
		{
			flag=1;
			while(temp>0)
			{
				int dig=temp%10;
				temp/=10;
				arr[dig]=1;
			}
			for(int k=0;k<10;k++)
			{
				if(!arr[k])
				{
					flag=0;
					break;
				}
			}
			if(flag)
			{
				cout<<"Case #"<<i<<": "<<num*j<<endl;
				break;
			}
			temp=num*(j+1);
		}

	}
}
