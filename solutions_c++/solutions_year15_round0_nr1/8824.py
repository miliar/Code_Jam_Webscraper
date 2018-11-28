#include<iostream>
#include<string>
#include<vector>

using namespace std;

int main()
{
	int t;
	cin>>t;
	int p = 1;
	while(t--)
	{
		int num;
		cin>>num;
		string s;
		cin>>s;
		int ans = 0;
		int tot = 0;
		for(int a = 0; a<s.length(); a++)
		{
			while(tot<a)
			{
				tot++;
				ans++;
			}
			tot = tot + (s[a]-'0');
		}
		cout<<"Case #"<<p<<": "<<ans<<"\n";
		p++;
	}
}

