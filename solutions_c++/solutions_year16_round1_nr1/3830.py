#include <bits/stdc++.h>
#define rep(i,a,b) for(int i=a;i<b;i++)

#define pb(u) push_back(u)

using namespace std;

int main()
{
	int t;
	scanf("%d",&t);

	for(int q=1;q<=t;q++)
	{

		string s;
		cin>>s;

		int n=s.size();

		string ans="";
		ans=ans+s[0];
		int k=0,l=0;
		for(int i=1;i<n;i++)
		{
			if(s[i]-'A' >= ans[l]-'A')
			{
				ans=s[i] + ans;
				
				

			}

			else{
				ans=ans+s[i];
				k=k+1;
				
			}

			
		}


















		cout<<"Case #"<<q<<": "<<ans<<endl;
	}
}