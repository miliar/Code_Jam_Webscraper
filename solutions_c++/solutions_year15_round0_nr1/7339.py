#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("abcdef.in","r",stdin);
    freopen("oo.out","w",stdout);
    int t;cin>>t;
    int caseno=0;
    while(t--)
    {
	++caseno;
	int n,i;cin>>n;
	string s;
	cin>>s;
	int m=s.size();
	int ans=0;
	int sum=0;
	int temp=0;
	for(i=0;i<m;i++)
	{
	    if(sum<i)
	    {
		temp++;
		ans+=temp;
	    }
	    if(temp)
	    {
	    	sum+=s[i]-'0'+temp;
		temp=0;
		continue;
	    }
	    sum+=s[i]-'0'+temp;
	}
	printf("Case #%d: %d\n",caseno,ans);
    }
    return 0;
}
