#include<iostream>
using namespace std;
int main()
{
	int n,i,x,num;
	int a[10];
	cin>>num;
	for(int j=0;j<num;++j)
	{
		cin>>n;
		cout<<"Case #"<<j+1<<": ";
		if(n==0)
		{
			cout<<"INSOMNIA\n";
			continue;
		}
		for(i=0;i<10;++i)
		a[i]=0;
		
		int count=0;
		x=n;
		while(count<10)
		{
			
			
			int t=x;
			while(t)
			{
				int r=t%10;
				t=t/10;
				if(a[r]==0)
				{
					a[r]=1;
					count++;
				}
				
			}
			x=x+n;
		}
		cout<<x-n<<'\n';
		
	}
}
