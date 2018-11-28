#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,len,i,s,ct,up,T;
	cin>>T;
	string st;
	for(t=1;t<=T;t++)
	{
	    cin>>s;
	    cin>>st;
	    ct=0;up=0;
	    len=st.length();
	    for(i=0;i<len;i++)
	    {
	    	if(st[i]!='0')
	    	{
	    		if(i>up)
	    		{
	    				ct=ct+(i-up);
	    			up=up+ct;
	    		}
	    	}
	    			up=up+(st[i]-48);
	
	    }
		cout<<"Case #"<<t<<": ";
		cout<<ct<<endl;
	}
	return 0;
}
