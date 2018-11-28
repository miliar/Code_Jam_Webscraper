#include <iostream>
#include <utility>
#include <queue>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for (int j=1;j<=t;j++)
	{
		cout<<"Case #"<<j<<": ";
		int n;
		cin>>n;
		priority_queue<pair<int,char> > q;
		for ( int i=0;i<n;i++)
		{
			int p;
			cin>>p;
			q.push(make_pair(p,(char)('A'+i)));
		}
		while(q.size()>0)
		{
			pair<int,char> p=q.top();
			q.pop();
			if(q.size()!=1)
			{
				cout<<p.second<<" ";
				p.first--;
				if (p.first>0) q.push(p);
			}
			else
			{
				pair<int,char> pp=q.top();
				q.pop();
				cout<<p.second<<pp.second<<" ";
				p.first--;
				pp.first--;
				if (p.first>0) q.push(p);
				if (pp.first>0) q.push(pp);
			}
		}
		cout<<endl;
	}
	return 0;
}