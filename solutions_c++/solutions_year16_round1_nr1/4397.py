#include<iostream>
#include<string.h>
#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
	int t;
	//	freopen("A-large.in","rt",stdin);
	//freopen("abhinavOutput.cpp","wt",stdout);
	cin>>t;
	for(int c=1;c<=t;c++)
	{
	    string s;
	    string s1;
	    cin>>s;
	    s1.insert(0,s,0,1);
	   // cout<<s1<<" ";
	    for(int i=1;i<s.length();i++)
	    {
	    	if(s[i]>=s1[0])
	    	{
	    		s1.insert(0,s,i,1);
	    		
	    	}
	    	else
	    	{
	    		s1.insert(s1.length(),s,i,1);
	    	//	cout<<s1<<" ";
	    	}
	    	
	    }
	
	    cout<<"Case #"<<c<<": "<<s1<<endl;
	    
	}
}
