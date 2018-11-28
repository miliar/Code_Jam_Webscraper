#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t,k=1;
	cin>>t;
	
	while(t--)
	{
		int smax,i,c=0,ans=0;
		cin>>smax;
		
		string s;
		cin>>s;
		
		for(i=0;i<(smax+1);i++)
		{
			int x = s[i] - '0';
		//	cout<<"x "<<x<<endl;
			if(i<=c)
			{
				c+=x;
			}
			else
			{
				if(x>0)
				{
					ans+= i-c;
					c+=(i-c);
					c+=x;
				}
			}
			//cout<<"d "<<c<<" "<<ans<<endl;
		}
		
		cout<<"Case #"<<k<<": "<<ans<<endl;
		k++;
	}
}
