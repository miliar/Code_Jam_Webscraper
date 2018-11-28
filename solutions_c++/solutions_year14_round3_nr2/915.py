#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cmath>
#include <numeric>
#include <algorithm>
#include <sstream>

#define INF 0x3f3f3f3f
#define NINF -0x3f3f3f3f

using namespace std;

typedef pair<int,int> pii;

long long cc;
int sol[100];
int visited[100];
char words[100][105];

void solve (int idx, int n)
{
	if (idx == n)
	{
		string s;
		for (int i = 0; i < n; i += 1)
		{
			s += words[sol[i]];
		}
		
		int used[28] = { 0 };
		used[s[0]-'a'] = true;
		
		for (int i = 1; i < s.size(); i += 1)
		{
			int ct = s[i]-'a';
			
			if (s[i] == s[i-1]) continue;
			
			if (used[ct]) return;
			used[ct] = true;
		}
		
		cc++;
		cc %= 1000000007;
		return;
	}
	
	for (int i = 0; i < n; i += 1)
	{
		if (visited[i]) continue;
		
		visited[i] = true;
		sol[idx] = i;
		solve(idx+1,n);
		visited[i] = false;
	}
}

void solveS (int t, int n)
{
	cc = 0;
	solve(0,n);
	
	printf("Case #%d: %lld\n",t,cc);
}

int main (int argc, char const* argv[])
{
	int T;
	scanf("%d",&T);
	
	for (int t = 1; t <= T; t += 1)
	{
		int n;
		scanf("%d",&n);
		
		for (int i = 0; i < n; i += 1)
		{
			scanf("%s",words[i]);
		}
		
		solveS(t,n);
	}
	
	return 0;
}
