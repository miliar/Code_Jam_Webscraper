#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t,i,j,k,l,ans;
    string str;
    cin>>t;
    for(i=0;i<t;i++){
    	cin>>j;
    	cin>>str;
    	l=0;
    	ans=0;
    	for(k=0;k<=j;k++)
    	{
    		if(l>=k)
    			l+=(str[k]-'0');
    		else
    		{
    			ans+=(k-l);
    			l+=(k-l);
    			l+=(str[k]-'0');
    		}	
    	}
    	cout<<"Case #"<<i+1<<": "<<ans<<endl;
    }
	return 0;
}