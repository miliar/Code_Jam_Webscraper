#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <cstdio>

using namespace std;

#define lli long long int
#define mod 1e9+7
#define rep(i,x,n) for(i=0;i<n;i++)

int main()
{
	std::ios_base::sync_with_stdio(false);
	lli test;
	cin>>test;
	for(int k=0;k<test;k++)
	{
		string s;
		char ans[1007];
		cin>>s;
		cout<<"Case #"<<k+1<<": ";
		ans[0]=s[0];
		int minn=0,max=0,i;
		for(i=1;i<s.length();i++)
		{
			if(s[i]>=ans[0]) 
			{
			    for(int j=strlen(ans);j>=1;j--)
			    {
			        ans[j]=ans[j-1];
			    }
			    ans[0]=s[i];
			}
			else ans[i]=s[i] ;
		}
		for(i=0;i<s.length();i++)
		    cout<<ans[i];
		cout<<endl;
	}
	return 0;
}