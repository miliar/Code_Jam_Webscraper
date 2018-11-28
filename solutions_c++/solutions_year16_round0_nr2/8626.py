#include <bits/stdc++.h>
using namespace std;
int main (int argc, char const* argv[])
{
	int t;
	cin>>t;
	for(int tc=1;tc<=t;tc++)
	{
		string s;
		cin>>s;
		int n = s.size();
		//cerr<<s<<" "<<n<<'\n';
		int ans =0 ;
		int f = 1;
		for (int i = 0; i < n; i += 1)if(s[i]=='-')f=0;
		while (!f)
		{
			//cerr<<"here "<<s<<" "<<ans<<'\n';
			int j=0;
			if(s[j]=='-')
			{
				while(j<n && s[j]=='-')s[j++]='+';
				ans++;
			}
			else
			{
				while(j<n && s[j]=='+')j++;
				while(j<n && s[j]=='-')s[j]='+',j++;
				ans += 2;
			}
			f = 1;
			for (int k = 0; k < n; k += 1)
			{
				if(s[k]=='-')f=0;
			}
		}
		cout<<"Case #"<<tc<<": "<<ans<<'\n';
	}
	return 0;
}
