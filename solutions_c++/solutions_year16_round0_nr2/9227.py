#include<bits/stdc++.h>
#define ll long long
#define ld long double
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define pp pair<ll,ll>
#define mm(a,b) memset(a,b,sizeof(a))

using namespace std;

int main()
{

	
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	
	int t;  string s;
	cin>>t;
	
	
	for(int cs=1;cs<=t;cs++)
	{
		cout<<"Case #"<<cs<<": ";
		
		
		int ans=0;
		cin>>s;
		
		while(s.size()>0)
		{
			
			while(s.size()>0 && s[s.size()-1]=='+')s.pop_back();
			
			if(s.size()==0)break;
			
			ans++;
			
			if(s[0]=='-')
			{
				reverse(s.begin(),s.end());
				
				for(int i=0;i<s.size();i++)
					s[i]=(s[i]=='+')?'-':'+';
					
			}
			else
			{
				int i=0;
				while(s[i]=='+')
				s[i++]='-';
			}
			
		}
			
		cout<<ans<<"\n";
		
		
	}
	


	return 0;
}


