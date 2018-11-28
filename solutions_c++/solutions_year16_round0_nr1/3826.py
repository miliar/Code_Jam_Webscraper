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
        int x;
        cin>>x;
        if(x==0)
        {
        	cout<<"Case #"<<cs<<": INSOMNIA";
        	cout<<"\n";
        	cs++;
        }
        else
        {
        	bool arr[10]={false},temp=false;
        	int count=1,y;
        	while(temp==false)
        	{
        		y=x*count;
        		while(y>0)
        		{
        			arr[y%10]=true;
        			y=y/10;
        		}
        		int i;
        		for(i=0;i<10;i++)
        		{
        			if(arr[i]==false)
        				break;
        		}
        		if(i==10)
        			break;
        		count++;
        	}
        	cout<<"Case #"<<cs<<": ";
	        cout<<x*count;
	        cout<<"\n";
	        cs++;
        }
        
    }
    
    return 0;
}
