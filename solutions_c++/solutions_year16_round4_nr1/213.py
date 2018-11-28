#include <cmath>
#include <cstdio>
#include <cstring>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <vector>
#include <string>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;

#define ALL(c) (c).begin(),(c).end()
#define SORT(a) sort(a.begin(), a.end())
#define UNIQ(a) a.resize(unique(a.begin(), a.end()) - a.begin())

string solve(char c0, int n)
{
	string s;
	string s1, s2;
	s += c0;
	if(n == 1)
		return s;

	if(c0 == 'P')
	{
		s1 = solve('P',n/2);
		s2 = solve('R',n/2);
	}
	if(c0 == 'R')
	{
		s1 = solve('R',n/2);
		s2 = solve('S',n/2);
	}
	if(c0 == 'S')
	{
		s1 = solve('P',n/2);
		s2 = solve('S',n/2);
	}
	if(s1 < s2)
		s = s1+s2;
	else
		s = s2+s1;
	return s;
}

int main() {
	int t;
	
	cin >> t;
	for(int tt=1; tt<=t; ++tt)
	{
		int n, R, P, S;
		cin >> n >> R >> P >> S;
		
		string ans = "";
		char psr[] = "PSR";
		for(int k=0; k<3; ++k)
		{
			string s = solve(psr[k], 1<<n);
			int m[256] = {0};
			for(int i=0; i<s.size(); ++i)
				++m[s[i]];
			if(m['P'] == P && m['R'] == R && m['S'] == S)
			{
				if(ans.empty() || s < ans)
					ans = s;
			}
		}

		if(ans.empty())
			ans = "IMPOSSIBLE";
		cout << "Case #" << tt << ": " << ans << "\n";
		cout.flush();
	}

	return 0;
}
