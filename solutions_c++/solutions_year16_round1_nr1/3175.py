#include <bits/stdc++.h>
using namespace std;

#define fr(a, n) for(a = 0; a < n; a++)
#define sc(a) scanf("%d", &a);
typedef pair<int, int> ii;
typedef pair<double, double> dd;

int main()
{
	int t, k;
	string a;
	deque<char> ans;
	string::iterator it;
	sc(t);
	fr(k,t)
	{
		cin>>a;
		ans.clear();
		for(it = a.begin(); it != a.end(); it++)
		{
			if(ans.empty()) ans.push_front(*it);
			else if(ans.front() <= *it) ans.push_front(*it);
			else ans.push_back(*it);
		}
		cout<<"Case #"<<k+1<<": ";
		while(!ans.empty())
		{
			cout<<ans.front();
			ans.pop_front();
		}
		cout<<'\n';
	}
	return 0;
}
