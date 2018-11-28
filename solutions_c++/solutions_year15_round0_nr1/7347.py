#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	cin>>t;
	int cas_no=0;
	while(t--)
	{
		int n;
		cin>>n;
		string str;
		cin>>str;
		int ans = 0, tot=0;
		for(int i=0;i<str.size();i++)
		{
			//cout<<i<<" "<<tot<<"\n";
			if(tot<i)
			{
				ans+= (i-tot);
				tot=i;
			}
			tot+= (str[i]-'0');
		}
		cout<<"Case #"<<++cas_no<<": ";
		cout<<ans<<"\n";
	}
	return 0;
}