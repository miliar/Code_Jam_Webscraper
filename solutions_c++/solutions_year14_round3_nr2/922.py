#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <cstring>
#include <vector>
#include <set>
#include <complex>

using namespace std;
#define rep(i,m) for(int i=0;i<m;i++)

#define SMALL_INPUT
//#define LARGE_INPUT

string compress(string s)
{
	vector<int> v(26, 0);
	string ret;//= "" + s[0];
	//	v[s[0] - 'a'] = 1;
	for (int i = 0; i < s.size(); ++i)
	{
		if (v[s[i] - 'a']) continue;
		ret += s[i];
		v[s[i] - 'a'] = 1;
	}
	if (s.size() > 0) ret += s[s.size() - 1];
	return ret;
}

bool check(string & s)
{
	vector<bool> vis(26, 0);
	vis[s[0] - 'a'] = 1;
	bool f = 1;
	for (int i = 1; i < s.size(); ++i)
	{
		if (s[i] != s[i - 1] && vis[s[i] - 'a'])
		{
			f = 0;
			break;
		}
		vis[s[i] - 'a'] = 1;
	}

	return f;
}

int main()
{
	freopen("b.in", "rt", stdin);
#ifdef SMALL_INPUT
	freopen("b-small-attempt1.in", "rt", stdin);
	freopen("b-small.txt", "wt", stdout);
#endif
#ifdef LARGE_INPUT
	freopen("b-large.in", "rt", stdin);
	freopen("b-large.txt", "wt", stdout);
#endif
	int tc;
	cin >> tc;
	rep(T,tc)
	{

		int n;
		cin >> n;
		vector<string> v(n);
		vector<int> ind(n);
		bool tmp = 0;
		for (int i = 0; i < n; ++i)
		{
			cin >> v[i];
			v[i] = compress(v[i]);
			tmp |= !check(v[i]);
			ind[i] = i;
		}
		//		for(int i=0;i<n;++i)
		//			for(int j=0;j<n;++j){
		//
		//			}
		if (tmp)
		{
			printf("Case #%d: %d\n", T + 1, 0);
			continue;
		}
		//sort(v.begin(), v.end());
		int cnt = 0;
		do
		{
			string s;
			for (int i = 0; i < n; ++i)
				s += v[ind[i]];

			bool f = check(s);
			cnt += f;
		} while (next_permutation(ind.begin(), ind.end()));
		printf("Case #%d: %d\n", T + 1, cnt);

#ifdef SMALL_INPUT
		cerr << T + 1 << " of " << tc << " is done." << endl;
#endif
#ifdef LARGE_INPUT
		cerr << T + 1 << " of " << tc << " is done." << endl;
#endif
	}
	return 0;
}
