#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pi;

#define MP make_pair
#define PB push_back
#define F first
#define S second
#define MOD 1000000007

int vis[1000001][2];

int rev(int n)
{
	int ans = 0, temp;
	while(n)
	{
		temp = n%10;
		n /= 10;
		ans = ans * 10 + temp;
	}
	return ans;
}

int bfs(int n)
{
	queue<pi> q;
	int cost = 1;
	q.push(MP(1, cost));
	memset(vis, 0, sizeof vis);
	pi temp;
	int n1, costify;
	while(!q.empty())
	{
		temp = q.front();
		q.pop();
		n1 = temp.F;
		costify = temp.S;
		if(n1 == n)
			break;
		if(vis[n1][0] && vis[n1][1] <= costify)
			continue;
		vis[n1][0] = 1;
		vis[n1][1] = costify;
		costify++;
		q.push(MP(n1 + 1, costify));
		q.push(MP(rev(n1), costify)); 
	}
	return costify;
}

int main()
{
	ios::sync_with_stdio(false);
	freopen("output1.txt", "w", stdout);
	freopen("A-small-attempt0.in", "r", stdin);
	int t, cases = 0;
	int n;
	cin >> t;
	while(t--)
	{
		cases++;
		cin >> n;
		cout << "Case #" << cases << ": " << bfs(n) << endl;
	}
	return 0;
}
