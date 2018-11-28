#include<bits/stdc++.h>
#define ll long long
using namespace std;
main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,t1,n,ans,count;
	char s[1001];
	cin>>t;
	t1=t;
	while(t--)
	{
		cin>>n>>s;
		count=s[0]-'0';
		ans=0;
		for(int i=1;i<=n;++i)
		{
			//cout<<count<<" ";
			if(count>=i)
			count+=s[i]-'0';
			else
			{
				ans+=i-count;
				count+=(i-count);
				count+=s[i]-'0';
			}
		}
		//cout<<endl;
		cout<<"Case #"<<t1-t<<": ";
		cout<<ans<<endl;
	}
}
