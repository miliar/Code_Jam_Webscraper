#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back

int main()
{
	int t,p=1;
	cin>>t;
	while(t--)
	{
		char s[1010],ans[1010];
		scanf("%s",s);
	    int n=strlen(s);
	    ans[0]=s[0];
	    for(int i=1;i<n;i++)
	    {
	    	if(ans[0]<=s[i])
	    	{
	    		for(int j=i;j>=0;j--)
	    		ans[j]=ans[j-1];
	    		ans[0]=s[i];
			}
			else 
			ans[i]=s[i];
		}
		cout<<"Case #"<<p<<": ";
		for(int i=0;i<n;i++)
		cout<<ans[i];
		cout<<"\n";
		p++;
	}
}
