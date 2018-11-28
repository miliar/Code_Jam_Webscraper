#include <bits/stdc++.h>
#define ll long long int

using namespace std;

string s;

int main()
{
	//ios_base::sync_with_stdio(false);
	int t,ans,len;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>s;
		len=s.length();
		ans=0;
		for(int j=0;j<len;j++)
		{
			ans++;
			while(j<len-1 && s[j+1] == s[j])
				j++;
		}
		if(s[len-1]=='+')
			ans-=1;
		cout<<"Case #"<<i<<": "<<ans<<"\n";
	}
	return 0;
}