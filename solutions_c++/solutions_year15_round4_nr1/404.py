#pragma comment (linker, "/STACK:268435456")
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <cmath>
#include <cctype>
#include <sstream>
#include <ctime>
#include <tuple>
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace __gnu_pbds;
using namespace std;
template <typename T> using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;
template <typename T> T sqr(T r) { return r * r; }

int check(vector<string> &a, int n, int m, int x, int y, int dx, int dy)
{
	if (x < 0 || x >= n || y < 0 || y >= m)
		return 0;
	if (a[x][y] != '.')
		return 1;
	return check(a, n, m, x + dx, y + dy, dx, dy);
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tn;
    cin >> tn;
    map<char, int> ddx, ddy;
    char pp[] = {'>', '^', '<', 'v'};
    ddx['>'] = 0; ddy['>'] = 1;
    ddx['^'] = -1; ddy['^'] = 0;
    ddx['<'] = 0; ddy['<'] = -1;
    ddx['v'] = 1; ddy['v'] = 0;
    for (int tc = 0; tc < tn; tc++)
    {
    	int n, m;
    	cin >> n >> m;
    	vector<string> a(n);
    	for (int i = 0; i < n; i++)
    		cin >> a[i];
    	int result = 0;
    	int fail = 0;
    	for (int i = 0; i < n; i++)
    		for (int j = 0; j < m; j++)
    			if (a[i][j] != '.')
    			{
    				if (check(a, n, m, i + ddx[a[i][j]], j + ddy[a[i][j]], ddx[a[i][j]], ddy[a[i][j]]))
    					;
    				else
    				{
    					int found = 0;
    					for (int k = 0; k < 4; k++)
    						found |= check(a, n, m, i + ddx[pp[k]], j + ddy[pp[k]], ddx[pp[k]], ddy[pp[k]]);
    					if (found)
    						result++;
    					else
    						fail = 1;
    				}
    			}
    	cout << "Case #" << tc + 1 << ": ";
    	if (fail)
    		cout << "IMPOSSIBLE";
    	else
    		cout << result;
    	cout << endl;
    }
    return 0;
}