#include<map>
#include<set>
#include<iostream>
#include<string.h>
#include<string>
#include<queue>
#include<cmath>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<memory.h>
#include <iomanip>
using namespace std;

#define mp make_pair
#define X first
#define Y second

double const eps = 1e-10;
int const INF = 100000;
int const MOD = 1;
int const MAX = 5*100*1000 + 5;

vector<int> v[105];
char temp[105];

void pr(char* s)
{
	int i, k, c, len = strlen(s);
	for(i = 1, k = 0, c = 1; i < len; ++i)
	{
		if(s[i] == s[i - 1])
			++c;
		else
		{
			v[k].push_back(c);
			c = 1;
			++k;
		}
	}
	v[k].push_back(c);
}

void trans(char* s)
{
	int k = unique(s, s + strlen(s))- s;
	s[k] = 0;
}

int main()
{
#ifdef _DEBUG
    freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);
#endif
	int t, tt, i, k, cnt, n;
	scanf("%d", &t);
	for(tt = 0; tt < t; ++tt)
	{
		for(i = 0; i < 105; ++i)
			v[i].clear();
		printf("Case #%d: ", tt + 1);
		scanf("%d", &n);
		bool f = false;
		char s[105];
		gets(s);
		gets(temp);

		pr(temp);
		trans(temp);		

		for(i = 1; i < n; ++i)
		{
			gets(s);
			pr(s);
			trans(s);
			if(strcmp(s, temp)!= 0)
			{
				puts("Fegla Won");
				f = true;
				break;				
			}
		}
		if(f)
			continue;
		int len = strlen(temp), ans = 0;
		for(k = 0; k < len; ++k)
		{
			int r = 1e3, sum = 0;

			for(i = 0; i < v[k].size(); ++i)
				sum += v[k][i];

			sort(v[k].begin(), v[k].end());
			for(i = 0; i < v[k].size(); ++i)
			{
				r = min(r, (2*i - (int)(v[k].size()))*v[k][i] + sum);
				sum += -2*v[k][i];				
			}
			ans += r;
		}
		printf("%d\n", ans);
	}

	return 0;
}