//be name khoda

#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t,j=0;
	cin>>t;
	j=t;
	while(t--)
	{
		int n,a[2000],o=0,ans=0;
		cin>>n;
		string s;
		cin>>s;
		for(int i=0;i<=n;i++)
		{
			ans=max(ans,i-o);
			o+=s[i]-'0';
		}
		cout<<"Case "<<"#"<<j-t<<": "<<ans<<endl;
	}
	return 0;
}
