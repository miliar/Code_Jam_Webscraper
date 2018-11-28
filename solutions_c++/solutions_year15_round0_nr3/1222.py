		//	   - -- --- ---- -----be name khoda----- ---- --- -- -		\\

#include <bits/stdc++.h>
using namespace std;

inline int in() { int x; scanf("%d", &x); return x; }
const int N = 20002;

int a[4][4] = {{0, 1, 2, 3},
			   {1, 0, 3, 2},
			   {2, 3, 0, 1},
			   {3, 2, 1, 0}};
int b[4][4] = {{1, 1, 1, 1},
			   {1, -1, 1, -1},
			   {1, -1, -1, 1},
			   {1, 1, -1, -1}};
int arr[N];
char c[N];
string s;

pair<int, int> zarb(int l, int r, int x = 1, int y = 0, bool p = 0)
{
	for(int i = l; i < r; i++)
		if(!p)
		{
			x *= b[y][arr[i]];
			y = a[y][arr[i]];
		}
		else
		{
			x *= b[arr[i]][y];
			y = a[arr[i]][y];
		}
	return {x, y};
}

int main()
{
	int _ = in();
	for(int i = 1; i <= _; i++)
	{
		printf("Case #%d: ", i);
		int n = in(), x = in();
		scanf("%s", c);
		string ss(c);
		s = string();
		while(x--)
			s += ss;
		n = s.size();
		for(int i = 0; i < n; i++)
			arr[i] = s[i] - 'i' + 1;
		auto kol = zarb(0, n);
		if(kol == pair<int, int>{-1, 0})
		{
			pair<int, int> have = {1, 0};
			int fi = n + 1, lk = -1;
			for(int i = 0; i < n; i++)
			{
				have = zarb(i, i + 1, have.first, have.second);
				if(have.first == 1 && have.second == 1)
				{
					fi = i;
					break;
				}
			}
			have = {1, 0};
			for(int i = n - 1; i >= 0; i--)
			{
				have = zarb(i, i + 1, have.first, have.second, 1);
				if(have.first == 1 && have.second == 3)
				{
					lk = i;
					break;
				}
			}
			if(fi < lk)
			{
				printf("YES\n");
				continue;
			}
		}
		printf("NO\n");
	}
}
