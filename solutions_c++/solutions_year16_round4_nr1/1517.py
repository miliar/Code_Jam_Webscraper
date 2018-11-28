#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <fstream>
#include <time.h>
#include <string>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <queue>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
using namespace std;


ifstream in("input.txt");
ofstream out("output.txt");
#define cin in
#define cout out
/**/
// rock paper scissors
char whoWin(char a, char b)
{
	if(a == 'P' && b == 'R')
		return 'P';
	if(a == 'P' && b == 'S')
		return 'S';
	if(a == 'R' && b == 'P')
		return 'P';
	if(a == 'R' && b == 'S')
		return 'R';
	if(a == 'S' && b == 'P')
		return 'S';
	if(a == 'S' && b == 'R')
		return 'R';
	return 'A';
}

bool dfs(int n, int i, int r, int p, int s, string & ans)
{
	if(i == (1<<n)+1)
	{
		string t = ans;
		for(int j = 0; j < n; ++j)
		{
			string cur;
			for(int i = 0; i < t.size(); i += 2)
			{
				if(t[i] == t[i+1])
					return false;
				cur += whoWin(t[i], t[i+1]);
			}
			t = cur;
		}
		return true;
	}

	if(p)
	{
		ans.push_back('P');
		if(dfs(n,i+1,r,p-1,s,ans))
			return true;
		ans.pop_back();
	}
	if(r)
	{
		ans.push_back('R');
		if(dfs(n,i+1,r-1,p,s,ans))
			return true;
		ans.pop_back();
	}
	
	if(s)
	{
		ans.push_back('S');
		if(dfs(n,i+1,r,p,s-1,ans))
			return true;
		ans.pop_back();
	}
	return false;
}

int main()
{
	int test;
	cin >> test;
	for(int _ = 1; _ <= test; ++_)
	{
		string ans;
		int n, r, p, s;
		cin >> n >> r >> p >> s;
		if(!dfs(n,1,r,p,s,ans))
			ans = "IMPOSSIBLE";
		cout << "Case #" << _ << ": " << ans << endl;
	}
	return 0;
}

/*
1 245
2 13
3 25
4 1
5 13

3 2 1 2 1

*/