#include<iostream>
#include<string>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int k=1;
	while(t--)
	{
		string s;
		int sm;
		cin>>sm>>s;
		//cout<<s<<"\n";
		int ct=s[0]-'0',ans=0;
		for(int i=1;i<=sm;i++)
		{
			if(ct<i)
			{
				ans+=(i-ct),ct+=(i-ct);
			}
			ct+=(s[i]-'0');
			//cout<<ans<<"\n";
		}
		cout<<"Case #"<<k<<": "<<ans<<"\n";
		k++;
	}
	return 0;
}