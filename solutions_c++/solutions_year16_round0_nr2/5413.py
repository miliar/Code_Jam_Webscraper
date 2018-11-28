#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll t,ans,n,c=0,chng,curr;
string str;

int main()
{
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	cin>>t;
	while(t--)
	{
		ans=0;
		chng=0;
		curr=0;
		c++;
		cin>>str;
		n=str.size();
		
		for(int i=n-1;i>=0;i--,curr=0)
		{
			if(str[i]=='-')
				curr=1;
			curr+=chng;
			if(curr%2)
			{
				ans++;
				chng++;
			}
		}
		
		cout<<"Case #"<<c<<": "<<ans<<endl;
	}
	return 0;
}
