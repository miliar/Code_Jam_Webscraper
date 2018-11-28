#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int q=1;q<=t;++q)
	{
		int ans=0,now=0;
		int smax;
		cin>>smax;
		string arr;
		cin>>arr;
		for(int i=0;i<=smax;++i)
		{
			ans+=max(0,i-now);
			now=max(now,i)+arr[i]-'0';
		}
		cout<<"Case #"<<q<<": "<<ans<<endl;
	}
	return 0;
}
