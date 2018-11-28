#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    int cs=1;
    while(t--)
    {
        string s;
        cin>>s;
        int count=0;
        for(int i=0;i<s.size();i++)
        {
        	if(s.at(i)=='-')
        	{
        		while(i<s.size()&&s.at(i)=='-')
        		{
        			i++;
        		}
        		i--;
        		count++;
        	}
        	else
        	{
        		if(i+1<s.size()&&s.at(i+1)=='-')
        			count++;
        	}
        }
        	cout<<"Case #"<<cs<<": ";
	        cout<<count;
	        cout<<"\n";
	        cs++;
    }
    
    return 0;
}
