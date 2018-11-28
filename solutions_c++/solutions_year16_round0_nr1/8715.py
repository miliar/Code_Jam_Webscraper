#include <iostream>
using namespace std;

int main() 
{
	int T;
	cin>>T;
	for(int k=1;k<=T;k++)
	{
		int n;
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<k<<": INSOMNIA"<<endl;
		}
		else
		{
			int a[10];
			for(int i=0;i<10;i++) a[i] = 0;
			int i;
			for(i=1;;i++)
			{
				int num = i*n;
				int flag = 0;
				for(int j=0;num!=0;j++)
				{
					if(num == 0) break;
					int rem = num%10;
					a[rem] = 1;
					num/=10;
				}
				for(int j=0;j<10;j++)
				{
					if(a[j]==0) 
					{
						flag = 1;
						break;
					}
				}
				if(flag == 1)
				{
					continue;
				}
				if(flag == 0)
				{
					break;
				}
			}
			cout<<"Case #"<<k<<": "<<i*n<<endl;
		}
	}
	return 0;
}
