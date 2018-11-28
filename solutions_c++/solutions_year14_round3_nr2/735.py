#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <iostream>
using namespace std;

char ss[105][105];
char s[105][105];
int sz[105];
int q[30];
int q1[30];

int mod = 1000000007;
int arr[105];

int main()
{
	//freopen("Binput.txt", "r", stdin);
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("Boutput.txt", "w", stdout);

	int T;
	cin >> T;
	for(int tt = 1; tt <= T; ++tt)
	{
		memset(ss, 0, sizeof(ss));
		memset(s, 0, sizeof(s));

		int n;
		cin >> n;
		for(int i = 0; i < n; ++i)
			scanf("%s", ss[i]);
		memset(q, 0, sizeof(q));

		for(int i = 0; i < n; ++i)
		{
			int l = strlen(ss[i]);
			s[i][0] = ss[i][0];
			s[i][1] = ss[i][l-1];
			sz[i] = min(l, 2);
			if(s[i][0] == s[i][1])
				sz[i] = 1;
			for(int j = 0; j < l; ++j)
				q[ss[i][j]-'a']++;
		}
		bool ok = 1;
		for(int i = 0; i < n && ok; ++i)
		{
			int l = strlen(ss[i]);
			if(l <= 2) continue;
			int j = 1;
			for(; j < l && ss[i][j] == ss[i][0]; ++j);
			if(ss[i][0] == ss[i][l-1] && j != l)
				ok = 0;
			for(; j < l-1;)
			{
				int qq = 0;
				char c = ss[i][j];
				for(; j < l && ss[i][j] == c; ++j, ++qq);
				if(j < l && qq < q[c-'a'])
				{
					ok = 0;
					break;
				}
			}						
		}
		if(!ok)
		{
			printf("Case #%d: 0\n", tt);
			continue;
		}

		memset(q, 0, sizeof(q));
		for(int i = 0; i < n; ++i)
			for(int j = 0; j < sz[i]; ++j)
				q[s[i][j]-'a']++;
		
		for(int i = 0; i < n; ++i)
			arr[i] = i;

		int ans = 0;
		do
		{
			bool ok1 = 1;
			memset(q1, 0, sizeof(q1));
			for(int i = 0; i < n; ++i)
			{
				int ai = arr[i];
				int ap = (i > 0 ? arr[i-1] : -1);
				
				if(ap >= 0 && s[ap][1] == s[ai][0])
					q1[s[ai][0] - 'a']++;
			}
			for(int i = 0; i < 26; ++i)
				if(q[i] > 1 && q[i] != q1[i]+1)
						ok1 = 0;
			ans += ok1;
			if(ans >= mod)
				ans -= mod;
		}
		while(next_permutation(arr, arr+n));

		printf("Case #%d: %d\n", tt, ans);		
	}
	
	return 0;
}