#include<iostream>
#include<vector>
#include<stack>
#include<cstring>
#include<map>
#include<set>
#include<string>
#include<queue>
#include<algorithm>
#include<stdio.h>
#include<sstream>
#include<cmath>
#include<cctype>
#include<fstream>
#include<set>
#define mp(x,y) make_pair(x,y)
using namespace std;
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.in","w",stdout);
	int t;
	cin>>t;
	int u=1;
	while(t--)
	{
		vector<int>a;
		vector<int>b;
		vector<vector<int> >adj(4,vector<int>(4));
		int s;
		cin>>s;
		for(int j=0;j<4;++j)
		{
			for(int k=0;k<4;++k)
			{
				cin>>adj[j][k];
				if(j==s-1)
					a.push_back(adj[j][k]);
			}
		}
		int s2;
		cin>>s2;
		for(int j=0;j<4;++j)
		{
			for(int k=0;k<4;++k)
			{
				cin>>adj[j][k];
				if(j==s2-1)
					b.push_back(adj[j][k]);
			}
		}
		cout<<"Case #"<<u++<<": ";
		int c=0;
		int v;
		for(int i=0;i<4;++i)
		{
			for(int j=0;j<4;++j)
			if(a[i]==b[j])
			{
				c++;
				v=a[i];
			}
		}
		if(c==1)
		{
			cout<<v<<endl;
		}
		if(c>1)
			cout<<"Bad magician!"<<endl;
		if(c==0)
			cout<<"Volunteer cheated!"<<endl;
	}
	return 0;
}
