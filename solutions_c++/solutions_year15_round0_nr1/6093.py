#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	ll t,s,t1=0;
	cin>>t;
	while(t1++<t)
	{
		cin>>s;
		char shy[1010];
		cin>>shy;
		int shyi[1010];
		
		for(int i=0;i<=s;i++)
			shyi[i]=shy[i]-'0';
			
		ll sum=0;
		ll count=0;	
			
		//if(shyi[0]==0)
		{
		//	count++;
		//	sum++;
		}	
		//sum+=shyi[0];
		for(int i=0;i<=s;i++)
		{
			
			if(sum<i)
			{
				count++;
				sum++;
			}
			sum+=shyi[i];
			//cout<<sum<<" "<<shyi[i]<<" "<<count<<endl;
			
		}
		cout<<"Case #"<<t1<<": "<<count<<endl;
		
	}
}
