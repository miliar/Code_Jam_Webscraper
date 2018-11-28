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

bool next(vector<int> & t, int n)
{
	++t[0];
	for(size_t i=0; i<t.size(); ++i)
	{
		if(t[i]==n)
		{
			t[i] = 0;
			if(i==t.size()-1)return false;
			else ++t[i+1];
		}
		else
		{
			break;
		}
	}
	return true;
}

int measure(const vector<int> & t, const vector<string> & sa)
{
	set<string> q;
	for(size_t v = 0; v<t.size(); ++v)
	{
		string s;
		for(size_t i=0; i<sa[t[v]].length(); ++i)
		{
			s.push_back(sa[t[v]][i]);
			q.insert(s);
		}
	}
	return q.size();
}

int get(const vector<vector<int> > & t, const vector<string> & s)
{
	int result = 0;
	for(size_t v = 0; v<t.size(); ++v)
	{
		if(t[v].empty())return 0;
		int locRes = measure(t[v], s) + 1;
		result += locRes;
	}
	return result;
}

void split(const vector<int> & t, vector<vector<int> > & ind)
{
	for(size_t i=0; i<t.size(); ++i)
		ind[t[i]].push_back(i);
}

void solve()
{
	int m, n; cin>>m>>n;
	vector<string> s(m); for(int i=0; i<m; ++i)cin>>s[i];
	vector<int> t(m);
	
	map<int, int> r;
	do
	{
		vector<vector<int> > ind(n);
		split(t, ind);
		int result = get(ind, s);
		++r[result];
	}
	while(next(t, n));

	cout<<r.rbegin()->first<<" "<<r.rbegin()->second<<endl;
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