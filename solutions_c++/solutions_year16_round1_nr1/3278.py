#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	for(int x=1;x<=t;x++)
	{
    	char s[1003],ans[2222];
    	int end=1101;
    	int start = 1100;
    	cin>>s;
    	cout<<"Case #"<<x<<": ";
	    int i=0;
	    ans[1100]=s[0];
	    
	    while(s[++i])
	    {
	        int j=start;
	        while(j<end && s[i]==ans[j])
	            j++;
	        if(s[i]>ans[j])
	        {
	            ans[--start]=s[i];
	        }
	        else
	            ans[end++]=s[i];
	    }
	    for(int k=start;k<end;k++)
	        cout<<ans[k];
	    cout<<endl;
	}
	return 0;
}

