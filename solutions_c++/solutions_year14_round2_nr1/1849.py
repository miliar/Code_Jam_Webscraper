#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>

using namespace std;

vector <char> ss[105];
int num[105][105];

int ABS(int x) { return x < 0 ? -x : x ; }
int main()
{
	freopen("1.txt", "r", stdin);
	freopen("2.txt", "w", stdout);
	int cas, T;
	
	for (cas = scanf("%d", &T); cas <= T; cas++)
	{
		int n;
		char str[105];
		cin >> n;
		
		for (int i = 1; i <= n; i++) ss[i].clear();
		memset(num, 0, sizeof(num));
		
		int mark = 0;
		for (int i = 1; i <= n; i++)
		{
			scanf("%s", str);
			for (int j = 0; str[j]; j++)
			{
				if (j == 0 || str[j] != str[j-1]) ss[i].push_back(str[j]);
				num[i][ss[i].size()] ++;
			}
			
			if (ss[i].size() != ss[1].size()) { mark = 1; continue ; }
			for (int j = 0; j < ss[1].size(); j++) if (ss[i][j] != ss[1][j]) mark = 1;
		}
		
		printf("Case #%d: ", cas);
		if (mark == 1) { puts("Fegla Won"); continue ; }
		
		int ans = 0;
		for (int i = 1; i <= ss[1].size(); i++)
		{
			int tmp = 200, mm = 0, mi = 200;
			for (int j = 1; j <= n; j++) mm = max(mm, num[j][i]) , mi = min(mi, num[j][i]);
			for (int j = mi; j <= mm; j++)
			{
				int now = 0;
				for (int k = 1; k <= n; k++) now += ABS(num[k][i] - j);
				tmp = min(tmp, now);
			}
			ans += tmp;
		}
		cout << ans << endl;
	}
	
	return 0;
}
