#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

#define pb push_back
#define mp make_pair
#define fs first
#define sc second

const double pi = acos(-1.0);
const int maxn = 5;
const int px4[] = {1, 0, -1, 0};
const int py4[] = {0, 1, 0, -1};
const int px8[] = {1, 1, 0, -1, -1, -1, 0, 1};
const int py8[] = {0, 1, 1, 1, 0, -1, -1, -1};

int cnt[maxn][maxn];
int n, m;

inline bool onfield(int n, int m, int x, int y) {
	return x >= 0 && y >= 0 && x < n && y < m;
}

vector <vector <vector <char> > > ans[maxn + 1][maxn + 1][maxn * maxn + 1];

int bitcount(int c) {
	int cnt = 0;
	while (c > 0) {
		cnt += c & 1;
		c /= 2;
	}

	return cnt;
}

vector <vector <char> > field(maxn);
bool used[maxn][maxn];
int hn, hm;

void dfs4(int x, int y) {
	if (field[x][y] == '#')
		return;
	used[x][y] = true;
	for (int i = 0; i < 4; i++)
		if (onfield(hn, hm, x + px4[i], y + py4[i]) && !used[x + px4[i]][y + py4[i]])
			dfs4(x + px4[i], y + py4[i]);
}

void dfs8(int x, int y) {
   	if (field[x][y] == '#')
		return;

	used[x][y] = true;
	if (cnt[x][y] == 0)
		for (int i = 0; i < 8; i++)
			if (onfield(hn, hm, x + px8[i], y + py8[i]) && !used[x + px8[i]][y + py8[i]])
				dfs8(x + px8[i], y + py8[i]);
}

bool connected(int n, int m) {
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			used[i][j] = false;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++) {
			if (field[i][j] == '.') {
	        	dfs4(i, j);
	        	bool flag = true;
	        	for (int p = 0; p < n; p++)
	        		for (int q = 0; q < m; q++)
	        			if (field[p][q] == '.' && !used[p][q])
	        				flag = false;
	        	return flag;
			}
		}
	return false;
}

bool verify(int n, int m, int x, int y) {
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++) {
			used[i][j] = false;
			cnt[i][j] = 0;
		}
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			if (field[i][j] == '*')
				for (int k = 0; k < 8; k++)
					if (onfield(n, m, i + px8[k], j + py8[k]))
						cnt[i + px8[k]][j + py8[k]]++;
	dfs8(x, y);
	bool flag = true;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			if (field[i][j] == '.' && !used[i][j])
				flag = false;
	return flag;
}

int main() {
	for (int i = 0; i < maxn; i++)
		field[i].resize(maxn);

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    for (int i = 1; i <= maxn; i++)
    	for (int j = 1; j <= maxn; j++)
    		for (int msk = 0; msk < (1 << (i * j)); msk++) {
    			int bc = bitcount(msk);
    			if (!ans[i][j][bc].empty())
    				continue;
    			for (int p = 0; p < i; p++) {
    				for (int q = 0; q < j; q++) {
    					field[p][q] = (((msk >> (p * j + q)) & 1) ? '*' : '.');
    			//    	cout << field[p][q];
    				}
    			//	cout << endl;
    			}
    			hn = i;
    			hm = j;
    			if (!connected(i, j))
    				continue;
    			//cerr << "ihere " << endl;
    			for (int p = 0; p < i; p++)
    				for (int q = 0; q < j; q++)
    					if (field[p][q] == '.' && ans[i][j][bc].empty() && verify(i, j, p, q) ) {
    						field[p][q] = 'c';
    				    	ans[i][j][bc].pb(field);
    					}
    		}

    int cur = 0;
    for (int i = 1; i <= maxn; i++)
    	for (int j = 1; j <= maxn; j++)
    		for (int k = 0; k < maxn * maxn; k++)
    			if (!ans[i][j][k].empty()) {
//    				cerr << i << ' ' << j << ' ' << k << endl;
    				cur++;
    			}
    cerr << endl << cur << endl;
    cerr << (clock() + 0.0) / CLOCKS_PER_SEC << endl;
//	return 0;
    int tc;

    int k;
    cin >> tc;
    for (int tnum = 0; tnum < tc; tnum++) {
    	cin >> n >> m >> k;
    	cerr << n << ' ' << m << ' ' << k << endl;
    	if (ans[n][m][k].empty()) {
    		cout << "Case #" << tnum + 1 << ":\nImpossible" << endl;
    	} else {
    		cout << "Case #" << tnum + 1 << ":" << endl;
        //	continue;
        	for (int i = 0; i < n; i++) {
        		for (int j = 0; j < m; j++)
        			cout << ans[n][m][k][0][i][j];
        		cout << endl;
        	}
    	}
    }

    cerr << (clock() + 0.0) / CLOCKS_PER_SEC << endl;

    return 0;
}