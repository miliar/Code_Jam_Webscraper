#include <iostream>
using namespace std;

int main()
{
	int t;
	cin>>t;
	int l=1;
	while(t--)
	{
		int x;
		cin>>x;
		char c[x+2];
		cin>>c;
		int ans=0;
		int total=c[0]-'0';
		for(int i=1;i<=x;i++)
		{
			if(total<i&&c[i]!='0')
			{
				int q=(i-total);
				total+=q;
				ans+=q;
			}
			int z=c[i]-'0';
			total+=z;
		}
		cout<<"Case #"<<l<<": ";
		l++;
		cout<<ans<<endl;
	}
	return 0;
}
