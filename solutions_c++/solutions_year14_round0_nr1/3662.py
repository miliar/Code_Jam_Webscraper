#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cmath>
#include<set>
using namespace std;

int main()
{
	int t,n,l,i,j,a,k;
	cin>>t;
	for(k=1;k<=t;k++)
	{
		set<int>s;
		int ans=0;
		cin>>n;
		for(i=1;i<=4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin>>a;
				if(i == n)
				{
					s.insert(a);
				}
			}
		}
		cin>>n;
		for(i=1;i<=4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin>>a;
				if(i == n)
				{
					l=s.size();
					s.insert(a);
					if(l == s.size())
					{
						ans=a;
					}
				}
			}
		}
		l=s.size();
		if(l == 7)
			cout<<"Case #"<<k<<": "<<ans<<endl;
		else if(l < 7)
			cout<<"Case #"<<k<<": Bad magician!"<<endl;
		else
			cout<<"Case #"<<k<<": Volunteer cheated!"<<endl;
		s.clear();
	}
}