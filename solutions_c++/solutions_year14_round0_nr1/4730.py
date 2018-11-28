#include <iostream>
#include <stdio.h>
#include <set>
#include <string.h>
#include <algorithm>
using namespace std;
set<int> g;
int main()
{
	int c;
	cin>>c;
	//cout<<c<<endl;
	int cc=1;
	while(c--)
	{
		printf("Case #%d: ",cc++);
		int k;
		cin>>k;
		g.clear();
		for(int i=0;i<4;i++)
		{
			int v;
			for(int j=0;j<4;j++)
			{
				cin>>v;
				if(i+1==k) g.insert(v);
			}
		}
		cin>>k;
		int cnt=0,sp;
		for(int i=0;i<4;i++)
		{
			int v;
			for(int j=0;j<4;j++)
			{
				cin>>v;
				if(i+1==k) 
				{
					if(g.count(v))
					{
						sp=v;
						cnt++;
					}
				}
			}
		}
		if(cnt==1)cout<<sp<<endl;
		else 
		if(cnt>1) puts("Bad magician!");
		else puts("Volunteer cheated!");
	}
	return 0;
}