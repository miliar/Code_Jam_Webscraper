#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	int cases=1;
	while(t--)
	{
		string s;
		cin>>s;
		char ch;
		long long int ans=0;
		for(int i=0;i<s.length();i++)
		{
			if(i==0)
				ch=s[i];
			while(i<s.length() && s[i]==ch)
			{
				i++;
			}
			if(i==s.length())
			{
				if(ch=='-')
					ans++;
				break;
			}
			i--;
			if(ch=='+')
			{
				ans++;
				ch='-';
			}
			else
			{
				ans++;
				ch='+';
			}
		}
		cout<<"Case #"<<cases<<": "<<ans<<"\n";
		cases++;
	}
	return 0;
}
