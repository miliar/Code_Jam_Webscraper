#include <bits/stdc++.h>
using namespace std;

inline char flip(char ch)
{
	if(ch=='+')
		return '-';
	return '+';
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int t;
	cin>>t;
	string str="Case #";
	int cnt=1;
	while(t--)
	{
		string s;
		cin>>s;

		int ans=0;
		string target="";
		int n=s.size();
		for(int i=1;i<=n;i++)
			target+='+';
		//cout<<target<<endl;
		while(s!=target)
		{
			ans++;
			char ch=s[0];
			int i=1;
			while(s[i]==ch&&i<n)
				i++;
			i--;
			for(int j=0;j<=i;j++)
				s[j]=flip(s[j]);
		}
		cout<<str<<cnt<<": "<<ans<<endl;
		cnt++;

	}

	return 0;
}