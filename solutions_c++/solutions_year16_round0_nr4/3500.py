#include <iostream>
using namespace std;

int main() {
	 freopen("D-small-attempt1.in","r",stdin);
  freopen("outputgcj_s4.out","w",stdout);
	int t,y,s,n,c;
	cin>>t;y=1;
	while(y<=t)
	{
		cin>>n>>c>>s;
		if(n==1)
		cout<<"Case #"<<y<<": 1"<<endl;
		else if(c==1)
		{
			if(s>=n)
			{cout<<"Case #"<<y<<": ";
			for(int i=1;i<=n;i++)
			{
				cout<<i<<" ";
			}
			cout<<endl;
			}
			else cout<<"Case #"<<y<<": IMPOSSIBLE"<<endl;
		}
		else 
		{   if(s>=n-1)
			{
			cout<<"Case #"<<y<<": ";
			for(int i=2;i<=n;i++)
		    {
		    
			cout<<i<<" ";
			}
			cout<<endl;
	       	
			}
			else 
			{
			cout<<"Case #"<<y<<": IMPOSSIBLE"<<endl;	
			}
		
			
		}
		y++;
	}
	
	
	
	return 0;
}
