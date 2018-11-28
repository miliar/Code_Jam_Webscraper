#include <iostream>
#include <algorithm>
#include <set>

using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int a=1;a<t+1;a++)
	{
		int r1,r2,num;
		bool found=false,bad=false;
		set<int> row1,row2;
		cin>>r1;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				cin>>num;
				if(i==(r1-1))
					row1.insert(num);
			}
		cin>>r2;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				cin>>num;
				if(i==(r2-1))
					row2.insert(num);
			}
		set<int>::iterator it;
		for(it=row1.begin();it!=row1.end();it++)
		{
			if(row2.find(*it)!=row2.end())
			{
				if(found)
					bad=true;
				if(!found)
				{
					found=true;
					num=*it;
				}
			}
		}
		if(bad)
			cout<<"Case #"<<a<<": "<<"Bad magician!\n";
		else if(!found)
			cout<<"Case #"<<a<<": "<<"Volunteer cheated!\n";
		else
			cout<<"Case #"<<a<<": "<<num<<"\n";
	}
}
