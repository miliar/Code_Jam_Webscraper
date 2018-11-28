#include <cstdio>
#include <iostream>
#include <vector>
#include <iterator>
#include <algorithm>
#include <cmath>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <stack>
 
using namespace std;

void solve()
{
	stack<int> q;
	int cnt = 0;
	int n, x; cin>>n>>x;

	vector<int> w(n);
	for(int i=0; i<n; ++i)cin>>w[i];
	sort(w.rbegin(), w.rend());

	for(int i=0; i<n; ++i)
	{
		int a = w[i];
		if(q.empty())q.push(a);
		else
		{
			int b = q.top();
			if(a+b<=x)
			{
				q.pop();
				++cnt;
			}
			else
			{
				q.push(a);
			}
		}
	}
	cout<<(q.size() + cnt)<<endl;
}

int main()
{
#ifdef GRANDVIC_DEBUG
	//freopen("i:/input.txt", "rt", stdin);
#endif
	ios_base::sync_with_stdio(0);
	int T; cin>>T;
	for(int t=1; t<=T; ++t)
	{
		cout << "Case #" << t << ": ";
		solve();
	}
	return 0;
} 