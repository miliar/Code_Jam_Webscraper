#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <memory>
#include <vector>
#include <string>
#include <bitset>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <climits>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <ctime>
#define sz(a) ((int)(a).size())
#define foreach(i, Type, v) for(Type::iterator i=v.begin(); i!=v.end(); i++)
using namespace std;
typedef long long llong;
typedef pair<int, int> Item;

const int Maxn = 100+10;
const int INF = 0x7f7f7f7f;
const double eps = 1e-10;
const double pi = acos(-1.0);
inline int compareTo(double a, double b) { return (a>b+eps) ? 1 : ((a+eps<b)?-1:0); }

int n, m, a[Maxn][Maxn];

bool solve(int h, int x, int y)
{
	bool row=true, col=true;
	for(int j=0; j<m; j++)
		if( a[x][j] > h )
			row = false;
	if( row )
		for(int j=0; j<m; j++)
			a[x][j] = min(h, a[x][j]);
	for(int i=0; i<n; i++)
		if( a[i][y] > h )
			col = false;
	if( col )
		for(int i=0; i<n; i++)
			a[i][y] = min(h, a[i][y]);
	return row||col;
}

int main()
{
	int cas;
	ios::sync_with_stdio(0);
	freopen("aaa.in", "r", stdin);
	freopen("aaa.out", "w", stdout);

	cin>>cas;
	for(int c=1; c<=cas; c++)
	{
		cin>>n>>m;
		int maxn = 0;
		vector<Item> vt[Maxn];
		for(int i=0; i<n; i++)
			for(int j=0; j<m; j++)
			{
				cin>>a[i][j];
				maxn = max(maxn, a[i][j]);
				vt[a[i][j]].push_back(Item(i, j));
			}
		bool flags = true;
		for(int h=maxn; h>=1; h--)
		{
			for(int k=0; k<sz(vt[h]); k++)
				if( !solve(h, vt[h][k].first, vt[h][k].second) )
				{
					flags = false;
					break;
				}
			if( !flags )
				break;
		}
		printf("Case #%d: ", c);
		/*for(int i=0; i<n; i++)
		{
			for(int j=0; j<m; j++)
				printf("%d ", a[i][j]);
			printf("\n");
		}*/
		if( flags )
			printf("YES\n");
		else
			printf("NO\n");
	}

	return 0;
}
