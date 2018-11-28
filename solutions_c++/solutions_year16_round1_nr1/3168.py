#include <bits/stdc++.h>
using namespace std;

int main() {
	long long t,i;
	cin>>t;
	for(long long j=1;j<=t;j++)
	{
	    
	    string s,s1;
	    cin>>s;
	    s1.insert(s1.begin(),s[0]);
	    for(i=1;i<s.length();i++)
	    {
	        if(s[i]>=s1[0])
	        {
	            s1.insert(s1.begin(),s[i]);
	        }
	        else
	        {
	            s1.insert(s1.end(),s[i]);
	        }
	        
	    }
	    cout<<"Case #"<<j<<": "<<s1<<"\n";
	}
	return 0;
}

