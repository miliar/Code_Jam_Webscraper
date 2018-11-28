#include <bits/stdc++.h>
using namespace std;
 
int main() {
	std::ios::sync_with_stdio(false);
	long long int t,k=1,c,f,s;
	
	/////////////////////////////////////////////
	cin>>t;
	
	while(k<=t)
	{
		cin>>f>>c>>s;
		
		if(f==1)
		cout<<"Case #"<<k<<": 1"<<endl;
 
		else if(c==1)
		{
			if(s>=f)
			{cout<<"Case #"<<k<<": ";
			for(long long int  j=1;j<=f;j++)
			{
				cout<<j<<" ";
			}
			cout<<endl;
			}
			else cout<<"Case #"<<k<<": IMPOSSIBLE"<<endl;
		}
		else 
		{   if(s>=f-1)
			{
			cout<<"Case #"<<k<<": ";
			for(long long int j=2;j<=f;j++)
		    {
 
			cout<<j<<" ";
			}
			cout<<endl;
 
			}
			
			else 
			{
			cout<<"Case #"<<k<<": IMPOSSIBLE"<<endl;	
			}
 
 
		}
		k++;
	}
 
 
 
	return 0;
}
