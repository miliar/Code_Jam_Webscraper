#include <iostream>
#include <queue>

using namespace std;

const int MAX = 1000110;

//int dp[MAX];

int myreverse(int n)
{
	if(n%10 == 0) return -1;
	int k=0;
	while(n>0)
	{
		k = k * 10 + n % 10;
		n/= 10;
	}
	return k;
}

//int f( int n)
//{
//	if(n == 1) return 1;
//	//if(low == n) return 0;
//	//int &ret = dp[low];
//	//if(ret != -1) return ret;
//	int x = myreverse(n);
//	if( x != -1 && x < n) return 1 + f(x);
//	return 1 + f(n-1);
//
//}

int bfs(int n)
{
	queue<pair<int, int> > q;
	q.push(make_pair(1,1));
	bool vis[MAX] = {true};
	while(! q.empty())
	{
		pair<int, int> u = q.front(); q.pop();
		int m = u.first;
		int depth = u.second;
		if(m == n) return depth;
		int x = myreverse(m);

		q.push(make_pair(m+1, depth+1));
		vis[m+1]=true;
		if(x != -1 && !vis[x] && x != m)
		{
			q.push(make_pair(x, depth +1));
			vis[x]=true;
		}

	}
	return -1;
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tnum;
	cin>>tnum;
	for(int q=1;q <= tnum;q++)
	{
		int n;
		cin>>n;
		cout << "Case #" << q << ": " << bfs(n) << endl;
	}
	
}