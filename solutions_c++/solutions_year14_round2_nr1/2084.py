#include <iostream>  
#include <algorithm>  
#include <cmath>  
#include <vector>  
#include <string>
#include <set>
using namespace std;  

int n,m,i,j,k,q,s,w,v,a[110],ans;
string t[110],p[110];
vector<int> l[110];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>w;
	for(v=1;v<=w;v++)
	{
		cin>>n;
		ans=0;
		for(i=0;i<=100;i++)
		{
			l[i].clear();
			t[i]="";
			p[i]="";
		}
		for(i=1;i<=n;i++)
			cin>>p[i];
		for(i=1;i<=n;i++)
		{
			for(j=0;j<p[i].length();j++)
			{
				t[i]+=p[i][j];
				q=1;
				while(j<p[i].length() && p[i][j]==p[i][j+1])
				{
					q++;
					j++;
				}
				l[i].push_back(q);
			}
		}
		for(j=0;j<t[1].length();j++)
		{
			for(i=2;i<=n;i++)
			{
				if(t[i][j]!=t[i-1][j] || l[i].size()!=l[i-1].size())
				{
					cout<<"Case #"<<v<<": "<<"Fegla Won"<<endl;
					goto verj;
				}
			}
		}
		for(j=0;j<t[1].length();j++)
		{
			q=0;
			for(i=1;i<=n;i++)
			{
				q+=l[i][j];
			}
			q=q/n;
			int pat2=0,pat1=0;
			for(i=1;i<=n;i++)
				pat1+=abs(q-l[i][j]);
			for(i=1;i<=n;i++)
				pat2+=abs(q+1-l[i][j]);
			ans+=min(pat1,pat2);
		}
		cout<<"Case #"<<v<<": "<<ans<<endl;
verj:;
	}
	return 0;
}






				






