#include <iostream>
#include <string>
using namespace std;

int main()
{
	int i,t,j;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		int ans = 0;
		string s;
		int x;
		cin>>x; //not required
		cin>>s;
		int m = 0; //standing person at this time
		for(j=0;j<s.size();j++)
		{
			if(m<j)
			{ //note that last d
				ans += j-m;
				m = j;
			}
			
			m += s[j]-'0';
		}
		cout<<"Case #"<<i<<": "<<ans<<'\n';
	}
	return 0;
}
