#include<bits/stdc++.h>

using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;i++)

int main()
{
	ios::sync_with_stdio(false);
	
	int t;
	cin>>t;
	FOR(i,1,t+1)
	{
		cout<<"Case #"<<i<<": ";
		
		int n;
		cin>>n;
		
		string s;
		cin>>s;
		
		int ct=0,ans=0;
		
		ct = s[0]-'0';
		
		FOR(i,1,n+1)
		{
			if(s[i] > '0')
			{
				if(ct >= i)
					ct+=s[i]-'0';
				else
				{
					ans+=(i-ct);
					ct = i;
					ct+=s[i]-'0';
				}
			}
		}
		
		cout<<ans;
		
		cout<<"\n";
	}	
		
	return 0;
}
