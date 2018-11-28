#include<iostream>
#include<vector>
#include<algorithm>
#include<string>

using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		string ans;
		int x,r,c;
		cin>>x>>r>>c;
		if((r*c)%x!=0)
		{
			ans="RICHARD";
		}	
		else 
		{
			if(x<=2)
			{
				ans="GABRIEL";
			}
			else if(x==3)
			{
				if((r*c)==3)
				{
					ans="RICHARD";
				}
				else
				{
					ans="GABRIEL";
				}
			}
			else if((r*c)==4 || (r*c)==8)
			{
				ans="RICHARD";
			}
			else if((r*c)==12 || (r*c)==16)
			{
				ans="GABRIEL";
			}
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;

	}
	return 0;
}