#include<iostream>
#include<cstdio>
#include <vector>
using namespace std;

int a,b,p[5],q[5],k,t;
vector <int> ans;
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	cin>>t;
	for(int g=0;g<t;g++)
	{
		cout<<"case #"<<g+1<<": ";
		cin>>a;
		for(int i=1;i<5;i++)
		{
			for(int j=1;j<5;j++)
			{
				if(i==a)cin>>p[j];
				else cin>>k;
			}
		}
		cin>>b;
		for(int i=1;i<5;i++)
		{
			for(int j=1;j<5;j++)
			{
				if(i==b)cin>>q[j];
				else cin>>k;
			}
		}
		for(int i=1;i<5;i++)
		{
			for(int j=1;j<5;j++)
			{
				if(p[i]==q[j])ans.push_back(p[i]);
			}
		}
		if(ans.size()==0) cout<<"Volunteer cheated!"<<endl;
		if(ans.size()>1) cout<<"Bad magician!"<<endl;
		if(ans.size()==1) cout<<ans[0]<<endl;
		ans.clear();
	}
	return 0;
}