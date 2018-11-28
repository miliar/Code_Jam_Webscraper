#include<iostream>
#include<cstring>
using namespace std;
int main()
{
	freopen("2input.txt","r",stdin);
    freopen("2out","w",stdout);
	int t,n,ans,people;
	string s;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		ans=0;people=0;
		cin>>n;  cin>>s;
		int l=s.length();
		for(int j=0;j<l;j++)
		{
			int x=s[j]-'0';
			
			if(i==0)
			{
				people=people+x;
				continue;
			}
			if(j<=people)
			{
				people=people+x;
				
			}
			else
			{
				ans=ans+j-people;
				people=people+x+(j-people);
			}	
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
		
		
		
		
		
	}
	
	
	
	return 0;
}
