#include <iostream>
#include <set>
using namespace std;
int main()
{
	int ans1,ans2,ans,count;
	set<int> s1;
	int t,x,num = 1;
	cin>>t;
	while(t--)
	{
		count = 0;
		s1.clear();
		cin>>ans1;
		for(int i = 1;i<=4;i++)
		{
			for(int j = 1;j <= 4;j++)
			{
				if(i == ans1)	//concerned row
				{
					cin>>x;
					s1.insert(x);
				}
				else
					cin>>x;
			}
		}
		cin>>ans2;
		for(int i = 1;i <=4;i++)
		{
			for(int j = 1; j <= 4;j++)
			{
				if(i == ans2)
				{
					cin>>x;
					if(s1.find(x) != s1.end())
					{
						count++;
						if(count == 1)	//this is the tentative answer
							ans = x;
					}
				}
				else
					cin>>x;
			}
		}
		if(count == 1)
		{
			cout<<"Case #"<<num<<": "<<ans<<endl;
		}
		else if(count > 1)
		{
			cout<<"Case #"<<num<<": "<<"Bad magician!"<<endl;
		}
		else if(count == 0)
		{
			cout<<"Case #"<<num<<": "<<"Volunteer cheated!"<<endl;	
		}
		num++;
	}
	return 0;
}