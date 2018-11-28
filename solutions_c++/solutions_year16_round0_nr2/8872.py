#include <bits/stdc++.h>
#define ll long long int
#define rep(a,c)   for ( ll (a)=0; (a)<(c); (a)++)
#define nl cout<<endl
using namespace std;

int main(){
	ll T,ans;
	char curr;
	string s;
	cin>>T;
	for (int t = 0; t < T; ++t)
	{
		/* code */
		cin>>s;
		ans=0;
		curr=s[0];
		for (int i = 0; i < s.size(); ++i)
		{
			/* code */
			if(curr!=s[i])ans++;
			curr=s[i];
		}
		if (curr!='+')ans++;
		cout<<"Case #"<<t+1<<": "<<ans<<endl;

	}


}