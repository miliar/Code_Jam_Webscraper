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
vector<bool>visit;
vector<double>g;
vector<double>b;
int n;
int main()
{
	freopen("D-large.in","r",stdin);
	freopen("out.in","w",stdout);
	int t;
	cin>>t;
	int u=1;
	while(t--)
	{
		cin>>n;
		g.clear();
		g.resize(n);
		b.clear();
		b.resize(n);
		vector<bool>v1(n);
		vector<bool>v2(n);
		visit.clear();
		visit.resize(n);
		for(int i=0;i<n;++i)
		{
			cin>>g[i];
		}
		for(int i=0;i<n;++i)
		{
			cin>>b[i];
		}
		sort(b.begin(),b.end());
		int b1=0,g1=0;
		for(int i=0;i<n;++i)
		{
			bool flag=0;
			v1[i]=1;
            for(int j=0;j<n;++j)
			{
				if(b[j]>g[i] && !v2[j])
				{
					flag=1;
					b1++;
					v2[j]=1;
					break;
				}
			}
			if(!flag)
			{
				for(int k=0;k<n;++k)
				{
					if(!v2[k])
					{
						v2[k]=1;
					    g1++;
						break;
					}
				}
			}
			
		}
		int g2=0;
		sort(g.begin(),g.end());
		v1.clear();
		v1.resize(n);
		v2.clear();
		v2.resize(n);
		for(int i=0;i<n;++i)
		{
			bool flag=0;
			v1[i]=1;
            for(int j=0;j<n;++j)
			{
				if(g[j]>b[i] && !v2[j])
				{
					flag=1;
					g2++;
					v2[j]=1;
					break;
				}
			}
			if(!flag)
			{
				for(int k=0;k<n;++k)
				{
					if(!v2[k])
					{
						v2[k]=1;
						break;
					}
				}
			}
			
		}
		cout<<"Case #"<<u++<<": ";
		cout<<g2<<" "<<g1<<endl;
	}
	return 0;
}
