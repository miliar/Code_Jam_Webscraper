#include<iostream>
#include<cstring>
#include<cstdio>
#include<vector>
#include<sstream>
#include<map>
#include<string>
#include<algorithm>
#include<set>
#include<list>
#include<stack>
#include<queue>
#include<deque>
#include<cmath>

using namespace std;
int main()
{
	int caso;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>caso;
	int t=1;
	while(t<=caso)
	{
		int n,var,m;
		map<int,int> dic;
		cin>>n;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>var;
				if((i+1)==n)
					dic[var]++;
			}
		}
		cin>>m;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>var;
				if((i+1)==m)
				{
					map<int,int>::iterator it = dic.find(var);
					if(it!=dic.end())
						dic[var]++;
				}
			}
		}
		int ans=0;
		int index;
		for(auto it= dic.begin();it!=dic.end();it++)
		{
			if(it->second>1)
			{
				index = it->first;
				ans++;
			}
		}
		if(ans==1)
			cout<<"Case #"<<t<<": "<<index<<endl;
		else if(ans>1)
			cout<<"Case #"<<t<<": "<<"Bad magician!"<<endl;
		else
			cout<<"Case #"<<t<<": "<<"Volunteer cheated!"<<endl;
		t++;
	}
}