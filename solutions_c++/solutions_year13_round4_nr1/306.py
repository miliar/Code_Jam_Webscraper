#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <cstring>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

#define mp make_pair
#define pb push_back

typedef long long lint;
typedef vector<int> vi;
typedef vector<string> vs;
const int INF = 0x7fffffff;

lint modul = 1000002013;

lint n;
lint calc(lint s1, lint s2)
{
	lint x = (2 * n + 1 - s2 + s1) * (s2 - s1) / 2;
	return x % modul;
}

int Solution()
{
	lint m;
	cin >> n >> m;
	set<lint> st;
	map<lint, lint> beg, end;
	lint ans1 = 0;
	for(int i = 0; i < m; ++i)
	{
		lint o, e, p;
		cin >> o >> e >> p;
		ans1 += p * calc(o, e) % modul;

		if(beg.find(o) == beg.end())
			beg[o] = p;
		else
			beg[o] += p;

		if(end.find(e) == end.end())
			end[e] = p;
		else
			end[e] += p;

		st.insert(o);
		st.insert(e);
	}

	lint ans2 = 0;
	set<pair<lint, lint> > peop;
	for(set<lint> :: iterator it = st.begin(); it != st.end(); ++it)
	{
		lint s = *it;
		if(beg.find(s) != beg.end())
			peop.insert(mp(s, beg[s]));
		
		lint exit = 0;
		if(end.find(s) != end.end())
			exit = end[s];
		
		set<pair<lint, lint> > :: iterator it2 = peop.end();
		while(exit > 0)
		{
			it2 --;

			lint s1 = (*it2).first;
			lint p1 = (*it2).second;
			if(p1 > exit)
			{
				ans2 += exit * calc(s1, s) % modul;
				p1 -= exit;
				exit = 0;
				peop.erase(it2);
				peop.insert(mp(s1, p1));
			}
			else
			{
				ans2 += p1 * calc(s1, s) % modul;
				exit -= p1;
				peop.erase(it2);
				it2 = peop.end();
			}
		}
	}

	lint ans = (ans1 - ans2) % modul;
	if(ans < 0)
		ans += modul;
	cout << ans;
	return 0;
}

#define debug 1

int main()
{
#ifdef debug
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif
	int n;
	cin >> n;
	getchar();
	for(int i = 1; i <= n; ++i)
	{
		printf("Case #%d: ", i);
		Solution();
		printf("\n");
	}
	return 0;
}
