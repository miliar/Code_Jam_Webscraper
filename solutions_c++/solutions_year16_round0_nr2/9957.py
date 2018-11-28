#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t, it;
	cin>>t;
    for(it=1; it<=t; it++)
	{
	    string s;
	    int ans, flag=0, i, f, count=0;
	    cin>>s;
	    if(s.at(0)=='-') flag=1;
	    i=0;
	    while(i<s.length())
	    {
	
	        if(s.at(i)=='-')
	        {
	            while(i<s.length() && s.at(i)=='-') i++;
	            count++;
	        }
	        else i++;
	    }
	    if(flag==0) ans=count*2;
	    else ans=(count*2)-1;
	    cout<<"Case #"<<it<<": "<<ans<<endl;
	       
	}
	return 0;
}
