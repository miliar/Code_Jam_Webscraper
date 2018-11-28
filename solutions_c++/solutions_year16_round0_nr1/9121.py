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

string to_s(int vl)
{
		stringstream ss ;
		ss << vl;            
		return ss.str();	
}

int main()
{
	
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	
	set<int> chk;
	int t,n;
	cin>>t;
			
	
	for(int cs=1;cs<=t;cs++)
	{
		
		chk.clear();

		cin>>n;
			
		if(n==0)
		{
			cout<<"Case #"<<cs<<": INSOMNIA\n";
			continue;	
		}	
			
		for(int j=1;j<=1000;j++)
		{
			
			string s=to_s(n*j);
			
			for(int k=0;k<s.size();k++)
				chk.insert(s[k]-'0');
			
			if(chk.size()==10)
			{
				cout<<"Case #"<<cs<<": "<<n*j<<"\n";
				break;
			}
		}
	
		
	}

}



