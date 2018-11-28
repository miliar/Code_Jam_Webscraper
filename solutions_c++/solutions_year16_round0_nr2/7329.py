#include<bits/stdc++.h>
typedef long long ll;
using namespace std;


int main()
{
	
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	ll t;
	cin>>t;
	for(ll i=0;i<t;i++)
	{
		string s;
		cin>>s;
		int l=s.length();
		ll ans=0;
		vector <int> a;
		for(int i=0;i<l;i++)
		{
			if(s[i]=='+')
			a.push_back(1);
			
			else
			a.push_back(0);
		}
		
		
		int vrcnt=0;
		
		while(vrcnt==0)
		{
			
		int localsum=0;
		for(int i=0;i<a.size();i++)
		{
			localsum+=a[i];
		}
		
		if(localsum==l)
		{
			cout<<"Case #"<<(i+1)<<": "<<0<<endl;
			goto label;
		}
		
		
		if(localsum==0)
		{
			cout<<"Case #"<<(i+1)<<": "<<1<<endl;
			goto label;
		}
		
		
		for(int i=a.size()-1;i>=0;i--)
		{
			
			if(a[i]==1)
			a.pop_back();
			
			else 
			break;
		}
		
		
		
		if(a[0]==1)
		{
			ans++;
			int k=0;
			while(a[k]==1)
			{
				a[k]=0;
				k++;
			}
		}
		
		
		
		if(a[0]==0)
		{
			ans++;
			vector <int>b;
			
			for(int i=a.size()-1;i>=0;i--)
			{
				
				b.push_back(1-a[i]);
				
			}
			
			
			
			for(int i=0;i<b.size();i++)
			a[i]=b[i];
			
			
			
			
		}
		
		
		
		int flag=0;
		for(int i=0;i<a.size();i++)
			{
				flag=0;
				if(a[i]==0)
				{
					flag=1;
					vrcnt=0;
					break;
				}
				
				
			}
			
			if(flag==0)
			{
				vrcnt=1;
				cout<<"Case #"<<(i+1)<<": "<<ans<<endl;
			}
		
		
		}
		
		label:
			{
				
			}
			
	}
	
	return 0;
}
	

