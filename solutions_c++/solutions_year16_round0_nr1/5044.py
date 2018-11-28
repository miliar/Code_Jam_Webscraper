#include <iostream>
using namespace std;
int main() {
	int t;
	cin>>t;
	//int a[201]={0};
	for(int i=1;i<=t;i++)
	{
		int n,ans;
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		bool b[10]={0};
		int c=10,x;
		for(int j=1;;j++)
		{
			x=n*j;
			while(x!=0)
			{
				int r=x%10;
				if(!b[r])
				{
					b[r]=1;
					c--;
				}
				x=x/10;
			}
			if(c==0)
			{
				ans=n*j;
				break;
			}
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}