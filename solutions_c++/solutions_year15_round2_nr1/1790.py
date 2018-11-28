#include<iostream>
#include<vector>
#include<queue>
#include<climits>
#define Size 1000001
using namespace std;
vector < int > vec[Size];
queue < int > que;
int vis[Size],arr[Size],ans[Size],Max=0,tc;
int height=1;
void bfs()
{
	int temp;
	int par=1;
	que.push(par);
	vis[par]=1;
	while(!que.empty())
	{
		par=que.front();
		for(int k=0;k<vec[par].size();k++)
		{
			if(!vis[vec[par][k]])
			{
				vis[vec[par][k]]=1;
				ans[vec[par][k]]=temp=ans[par]+1;
				height=(height>temp)?height:temp;	
				que.push(vec[par][k]);
			}
		}
		que.pop();
	}
}
int main()
{
	cin >> tc;
	for(int i=0;i<tc;i++)
		cin >> arr[i];
	for(int i=1;i<=Size-1;i++)
	{
		ans[i]=1;
		int n=i,rev=0;
		while(n)
		{
			rev=rev*10+n%10;
			n=n/10;
		}
		if(rev!=i)
			vec[i].push_back(rev);
		if(i+1<=Size-1)
			vec[i].push_back(i+1);
	}
	bfs();
	for(int i=0;i<tc;i++)
		cout << "Case #" << i+1 << ": " << ans[arr[i]] << endl;	
	return 0;
}
