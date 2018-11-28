#include<bits/stdc++.h>
#include<string>
using namespace std;
int main()
{
    freopen("input.in", "r", stdin);
    freopen("out.txt", "w", stdout);
	int t,sm,i,x=1;
	string s;
	cin>>t;
	while(x<=t)
	{
		cin>>sm;
		cin>>s;
		int a[sm+1],f=0,c=0;
		
		for(i=0;i<=sm;i++)
		{
			a[i]=s[i]-48;
			
			if(c>=i || a[i]==0)
			{
			    c += a[i];
			}
			else
			{
				f += i-c;
			   	c = c+f+a[i];
			}
		}
		
		cout<<"Case #"<<x<<": "<<f<<"\n";
		 x++;
	}
	return 0;
}
