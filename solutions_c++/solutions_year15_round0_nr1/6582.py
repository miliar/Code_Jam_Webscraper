#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	for(int c=1;c<=t;c++) 
	{
		 int smax;
		 string s;
		 cin>>smax;
		 cin>>s;
		
		
		int ss=0;
		int ans=0;
	    
	    for(int i=0;i<smax;i++)
	    {
	    	ss+=(s[i]-48);
	    	if(ss<i+1)
	    	{
	    	ans++;
	    	ss++;
	    	}
	    }
		cout<<"Case #"<<c<<": "<<ans<<endl;
		
		
	}
	return 0;
}