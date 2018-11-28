#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("inl.in","r",stdin);
	freopen("out.txt","w",stdout);
	int n;
	cin>>n;
	int c_number=0;
	while(n--)
	{
		c_number++;
		int x;
		cin>>x;
		int arr[10]={0};
		int count=0;
		if(x==0)
		cout<<"Case #"<<c_number<<": "<<"INSOMNIA"<<endl;
		else
		{
			int p=1;
			while(count<10)
			{
				int temp=x*p;
				while(temp>0)
				{
					int digit = temp%10;
					if(arr[digit]==0)
					{
						arr[digit]=1;
						count++;
					}
					temp/=10;
				}
				p++;	
			}	
			cout<<"Case #"<<c_number<<": "<<x*(p-1)<<endl;
		}
	}
	return 0;
}
