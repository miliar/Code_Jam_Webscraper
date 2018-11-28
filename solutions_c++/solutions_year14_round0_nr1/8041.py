#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>
#include<cstring>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int te=1;te<=t;te++)
	{
		int x,y,a[4];
		cin>>x;
		x--;
		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		{
			if(i==x)
			cin>>a[j];
			else
			cin>>y;
		}
		//for(int i=0;i<4;i++)
		//cout<<a[i]<<endl;
		cin>>y;
		y--;
		int flag=0,ans;
		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		{
			if(i==y)
			{
				cin>>x;
				for(int k=0;k<4;k++)
				if(a[k]==x)
				flag++,ans=x;
			}
			else
			cin>>x;
		}
		if(flag==0)
		cout<<"Case #"<<te<<": Volunteer cheated!"<<endl;
		else if(flag==1)
		cout<<"Case #"<<te<<": "<<ans<<endl;
		else
		cout<<"Case #"<<te<<": Bad magician!"<<endl;
	}
	return 0;
}
