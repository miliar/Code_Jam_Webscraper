#include <iostream>
using namespace std;

int main()
{
	long long int t,n,ans,curr,i,tt;
	string s;
	cin>>t;
	tt=1;
	while (tt<=t)
	{
		cin>>n;
		cin>>s;
		ans=0;
		curr=0;
		for (i=0;i<s.length();i++)
		{
			if (curr < i)
			{
				ans+=(i-curr);
				curr+=(i-curr);
			}
			curr+=(s[i]-'0');
		}
		cout<<"Case #"<<tt<<": "<<ans<<endl;
		tt+=1;
	}
	return 0;
}