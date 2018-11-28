#include<iostream>
#include<queue>
using namespace std;
int a[1000002][2];
int vis[1000002];
int mic;
queue<pair<int,int> > q;
int bfs(int n)
{
	q.push(make_pair(1,1));
	vis[1]=1;
	while(!q.empty())
	{
		pair<int,int> p=q.front();
//		cout<<p.first<<" "<<a[p.first][0]<<" "<<a[p.first][1]<<endl;
		if(p.first==n)
			return p.second;
		if(vis[a[p.first][0]]==0)
		{
			vis[a[p.first][0]]=1;
			q.push(make_pair(a[p.first][0],p.second+1));
		}
		if(vis[a[p.first][1]]==0)
		{
			vis[a[p.first][1]]=1;
			q.push(make_pair(a[p.first][1],p.second+1));
		}
		q.pop();
	}
}
int main()
{
	for(int i=1;i<=1000001;i++)
	{
		a[i][0]=i+1;
		int d=i,p=0;
		while(d!=0)
		{
			p=p*10+d%10;
			d/=10;
		}
		a[i][1]=p;
//		cout<<i<<" "<<a[i][0]<<" "<<a[i][1]<<endl;
	}
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int n;
		cin>>n;
		for(int j=1;j<=1000001;j++)
			vis[j]=0;
		cout<<"Case #"<<i<<": "<<bfs(n)<<endl;
		while(!q.empty())
			q.pop();
	}
//	cout<<mac<<endl;
	return 0;
}
