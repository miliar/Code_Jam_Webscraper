#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <list>
#include <stack>
#include <set>
#include <map>

using namespace std;


int main()
{	
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int cases;
	cin>>cases;
	for (int curcase=1;curcase<=cases;curcase++)
	{
		cout<<"Case #"<<curcase<<": ";
		{
			int currow;
			cin>>currow;
			int d[4][4];
			for (int i=0;i<4;i++)
			{
				for(int j=0;j<4;j++)
				{
					cin>>d[i][j];
				}
			}
			set<int> s;
			for (int j=0;j<4;j++)
			{
				s.insert(d[currow-1][j]);
			}
			cin>>currow;
			for (int i=0;i<4;i++)
			{
				for(int j=0;j<4;j++)
				{
					cin>>d[i][j];
				}
			}
			set<int> cdts;
			for (int j=0;j<4;j++)
			{
				if (s.count(d[currow-1][j]))
					cdts.insert(d[currow-1][j]);
			}
			if (cdts.size()==0)
			{
				cout<<"Volunteer cheated!";
			}
			if (cdts.size()>1)
			{
				cout<<"Bad magician!";
			}
			if (cdts.size()==1)
			{
				cout<<*cdts.begin();
			}
		}
		cout<<"\n";
	}
	return 0;
}
