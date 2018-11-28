#include <iostream>
#include <set>

using namespace std;

int main()
{
	int t=0;
	cin>>t;
	for(int m=0;m<t;m++)
	{
		int a,last,count=0;
		set<int> res;
		cin>>a;
		for(int i=0;i<4;i++)
		{
			
			for(int j=0;j<4;j++)
			{
				int h;
				cin>>h;
				if(i==a-1)
				{
					
					res.insert(h);
				}
			}
		}
		cin>>a;
		for(int i=0;i<4;i++)
		{
			
			for(int j=0;j<4;j++)
			{
				int h;
				cin>>h;
				if(i==a-1)
				{
					if(res.find(h)!=res.end())
					{
						count++;
						last=h;
					}
				}
			}
		}
		cout<<"Case #"<<m+1<<": ";
		if(count==0)
		{
			cout<<"Volunteer cheated!"<<endl;
		}
		else if(count==1)
		{
			cout<<last<<endl;
		}
		else
		{
			cout<<"Bad magician!"<<endl;
		}
	}
}
