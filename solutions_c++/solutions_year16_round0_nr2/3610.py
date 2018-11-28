#include <bits/stdc++.h>
using namespace std;

int main() {
    std::ios::sync_with_stdio(false);
	long long t;
	string s;
	cin>>t;
	for(long long i=1;i<=t;i++)
	{
	    long long count=0;
	    cin>>s;
	    if(s[0]=='-')
	    count=1;
	    for(long long j=0;j<s.length()-1;j++)
	    {
	        if(s[j]=='+'&&s[j+1]=='-')
	        count++;
	    }
	    if(s[0]=='-')
	    cout<<"Case #"<<i<<": "<<2*count-1<<"\n";
	    else
	    cout<<"Case #"<<i<<": "<<2*count<<"\n";
	}
	return 0;
}