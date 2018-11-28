#include <cstdio>
#include <algorithm>
#include <queue>

using namespace std;

int a[128][128];

int main()
{
	int tn;
	int ti = 0;
	scanf("%d", &tn);
	while(tn--)
	{
		int n, m;
		priority_queue<int, vector<int>, greater<int> > q;
		scanf("%d %d", &n, &m);
		for(int i = 0; i < n; ++i)
			for(int j = 0; j < m; ++j)
			{
				scanf("%d", &a[i][j]);
				q.push(a[i][j]);
			}
		bool changed = true;
		while(changed)
		{
			changed = false;
			int t = q.top();
			for(int i = 0; i < n; ++i)
			{
				int w = 0;
				for(int j = 0; j < m; ++j)
				{
					if(a[i][j] == 0) continue;
					if(a[i][j] == t) 
						w = a[i][j];
					else 
					{
						w = 0;
						break;
					}
				}
				if(w > 0) 
				{
					for(int j = 0; j < m; ++j)
					{
						if(a[i][j]  > 0) 
						{
							a[i][j] = 0;
							q.pop();
						}
					}
					changed = true;
				}
			}
			for(int i = 0; i < m; ++i)
			{
				int w = 0;
				for(int j = 0; j < n; ++j)
				{
					if(a[j][i] == 0) continue;
					if(a[j][i] == t)
						w = a[j][i];
					else 
					{
						w = 0;
						break;
					}
				}
				if(w > 0) 
				{
					for(int j = 0; j < n; ++j)
						if(a[j][i] > 0)
						{
							a[j][i] = 0;
							q.pop();
						}
					changed = true;
				}
			}
		}
		bool possible = true;
		for(int i = 0; i < n; ++i)
			for(int j = 0; j < m; ++j)
				if(a[i][j] != 0) possible = false;
		printf("Case #%d: ", ++ti);
		if(possible) printf("YES\n");
		else printf("NO\n");
	}
}
