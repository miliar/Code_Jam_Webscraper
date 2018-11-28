#include <iostream>
#include <stdio.h>
#include <string>
#include <ctype.h>
#include <stdlib.h>
#include <math.h>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <utility>
#include <map>
// #include <unordered_map>
#include <vector>
#include <list>
#include <string>
#include <set>
#include <stack>
#include <queue>
#include <deque>
#include <climits>
#include <limits.h>
 
#define MOD 1000000007 
 
typedef long long LL;
 
using namespace std;
 
LL gcd(LL u, LL v)
{
	return (v != 0)?gcd(v, u%v):u;
}

bool done(string s)
{
	int len = s.length();
	for(int i=0;i<len;++i)
	{
		if(s[i]=='-')return false;
	}
	return true;
}

void flip(string &s)
{
	int len = s.length();
	char start = s[0];
	for(int i=0;i<len && s[i]==start;++i)
	{
		if(s[i]=='+')s[i]='-';
		else s[i]='+';
	}
}

int main()
{
	int t;
	cin>>t;		
	for(int tc=1;tc<=t;tc++)
	{
		string s;
		cin>>s;

		int ans = 0;
		while(!done(s))
		{
			ans++;
			flip(s);
		}

		printf("Case #%d: %d\n", tc,ans);		
	}

	return 0;
}
