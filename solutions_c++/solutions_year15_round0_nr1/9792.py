#include<bits/stdc++.h>
using namespace std;
#define ll long long 
int main()
{
	int t,n;
	ll ans,tmp,x=1;
	string s;
	scanf("%d",&t);
	while(t--)
	{
		ans=tmp=0;
		cin>>n;
		cin>>s;
		for(int i=0 ; i<=n ; ++i)
		{	
				if(tmp<(i) && (s[i])!='0')
				{
					ans+=(i-tmp);
					tmp+=ans;
				}
				tmp+=s[i]-48;
		}
		cout<<"Case #"<<x<<": "<<ans<<endl;
		x++;
	}
	return 0;
}
