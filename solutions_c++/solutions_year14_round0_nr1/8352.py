#include <iostream>
#include <iomanip>
#include <cmath>
#include <list>
#include <stack>
#include <queue>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

int main()
{
	//freopen("a.in","r",stdin);
	//freopen("a.out","w",stdout);
	int cases,ans,temp,res,c;
	bool flag[20];
	cin>>cases;
	for(int kase=1;kase<=cases;kase++)
	{
		for(int i=1;i<=16;i++)
		{
			flag[i]=false;
		}
		cin>>ans;
		for(int i=1;i<=4;i++)
		{
			if(i==ans)
			{
				for(int j=1;j<=4;j++)
				{
					cin>>temp;
					flag[temp]=true;
				}
			}
			else
			{
				for(int j=1;j<=4;j++)
				{
					cin>>temp;
				}
			}
		}
		cin>>ans;
		c=0;
		for(int i=1;i<=4;i++)
		{
			if(i==ans)
			{
				for(int j=1;j<=4;j++)
				{
					cin>>temp;
					if(flag[temp])
					{
						res=temp;
						c++;
					}
				}
			}
			else
			{
				for(int j=1;j<=4;j++)
				{
					cin>>temp;
				}
			}
		}
		cout<<"Case #"<<kase<<": ";
		if(c==1)
		{
			cout<<res<<"\n";
		}
		else if(c==0)
		{
			cout<<"Volunteer cheated!\n";
		}
		else
		{
			cout<<"Bad magician!\n";
		}
	}
	return 0;
}