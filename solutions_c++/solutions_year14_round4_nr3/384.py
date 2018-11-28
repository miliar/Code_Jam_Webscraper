#pragma comment(linker, "/STACK:1000000000")
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
const int size = 1000;
const int px[] = {1, 0, -1, 0};
const int py[] = {0, 1, 0, -1};

bool used[size][size];
int w, h, n;
int tc;
int xc1[size], yc1[size], xc2[size], yc2[size];

bool onfield(int x, int y) {
	return x >= 0 && y >= 0 && x < w && y < h && !used[x][y];
}

bool dfs(int x, int y, int d) {
	//cerr << x << ' ' << y << endl;
	if (y == h - 1) {
		used[x][y] = true;
		return true;
	}
	used[x][y] = true;
	for (int i = 1; i >= -1; i--) {
	    int nw = (d + i + 4) % 4;
	    int nx = x + px[nw];
	    int ny = y + py[nw];
		if (onfield(nx, ny) && dfs(nx, ny, nw))
			return true;
	}
	//used[x][y] = false;
	return false;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> tc;
    for (int tnum = 0; tnum < tc; tnum++) {
        cerr << tnum << endl;
    	cin >> w >> h >> n;
    	for (int i = 0; i < w; i++)
    		for (int j = 0; j < h; j++)
    			used[i][j] = false;
    	for (int i = 0; i < n; i++) {
    		cin >> xc1[i] >> yc1[i] >> xc2[i] >> yc2[i];
    		for (int p = xc1[i]; p <= xc2[i]; p++)
    			for (int q = yc1[i]; q <= yc2[i]; q++)
    				used[p][q] = true;
    	}

    	int ans = 0;
    	for (int i = 0; i < w; i++)
    		if (onfield(i, 0))
	    		ans += dfs(i, 0, 1);
    	cout << "Case #" << tnum + 1 << ": " << ans << endl;
    }

    return 0;
}