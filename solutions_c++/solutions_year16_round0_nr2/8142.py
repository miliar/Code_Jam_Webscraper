#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	for(int T=1;T<=t;T++)
	{
		string s;
		cin>>s;
		int i,n=s.size();
		if(count(s.begin(),s.end(),'+')==n)
	     	printf("Case #%d: 0",T);
	    else if(count(s.begin(),s.end(),'-')==n)
	     	printf("Case #%d: 1",T);
	    else
	    {
	    	int ans=0;
	    	for(i=0;i<n-1;i++)
	    	{
	    		if(s[i]!=s[i+1])
	    		ans++;
			}
			if(s[n-1]=='-')
			ans++;
			printf("Case #%d: %d",T,ans);
		}
		printf("\n");
	}
	return 0;
}
