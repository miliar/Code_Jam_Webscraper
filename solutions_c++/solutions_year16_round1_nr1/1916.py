#include <iostream>
#include <vector>
#include <string>
using namespace std;
int main()
{
	int t;
	cin>>t;
	//////////////

	for(int i=1;i<=t;i++)
	{
		string x;cin>>x;
		string ans;
		ans=x[0];
		for(int i=1;i<x.length();i++)
		{
			if(x[i]>=ans[0])
				ans=x[i]+ans;
			else 
				ans=ans+x[i];
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;///////////
	}
}