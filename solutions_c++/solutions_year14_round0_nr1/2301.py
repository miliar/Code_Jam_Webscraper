#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;
 

 
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int arr[4][4],arr2[4][4];
	int a,b,c,d;
	int tc;
	cin>>tc;
	for(int i=1;i<=tc;i++)
	{
		cin>>a;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				cin>>arr[j][k];
		cin>>b;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				cin>>arr2[j][k];
		map<int,int>ma;
		for(int j=0;j<4;j++)
		{
			ma[arr[a-1][j]]++;
			ma[arr2[b-1][j]]++;
		}
		c=0;
		map<int,int>::iterator it;
		for(it=ma.begin();it!=ma.end();it++)
		{
			if(it->second>=2)
			{
				c++;
			d=it->first;
			}
		}
		cout<<"Case #"<<i<<": ";
		if(c>1)
			cout<<"Bad magician!"<<endl;
		else if(c==1)
			cout<<d<<endl;
		else cout<<"Volunteer cheated!"<<endl;
	}
	return 0;
}
