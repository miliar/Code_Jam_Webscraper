#include <iostream>
#include <fstream>
#include <vector>
#include <stack>
#include <queue>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>

using namespace std;

typedef long long ll;
typedef pair<int,int> PP;

/*
    freopen("input","r",stdin);
    freopen("output","w",stdout);
*/

int R,C;
vector<vector<char> > M;

int solve() {
	int i,j,k,n,m;
	int res = 0;
	bool ok;
    for (i = 0;i < R;i++) {
    	for (j = 0;j < C;j++) {
    		if (M[i][j] != '.') {
    			ok = 0;
    			for (n = 0;n < R;n++) {
    				if (n == i) continue;
    				if (M[n][j] != '.') ok = 1;
    			}
    			for (n = 0;n < C;n++) {
    				if (n == j) continue;
    				if (M[i][n] != '.') ok = 1;
    			}
    			if (ok == 0) {
    				return -1;
    			}
    			if (M[i][j] == '<') {
    				ok = 0;
    				for (n = 0;n < j;n++) {
    					if (M[i][n] != '.') ok = 1;
    				}
    				if (ok == 0) res++;
    			}
    			if (M[i][j] == '>') {
    				ok = 0;
    				for (n = j + 1;n < C;n++) {
    					if (M[i][n] != '.') ok = 1;
    				}
    				if (ok == 0) res++;
    			}
    			if (M[i][j] == '^') {
    				ok = 0;
    				for (n = 0;n < i;n++) {
    					if (M[n][j] != '.') ok = 1;
    				}
    				if (ok == 0) res++;
    			}
    			if (M[i][j] == 'v') {
    				ok = 0;
    				for (n = i + 1;n < R;n++) {
    					if (M[n][j] != '.') ok = 1;
    				}
    				if (ok == 0) res++;
    			}
    		}
    	}
    }
    return res;
}

int main() {
	freopen("A-large.in.txt","r",stdin);
    freopen("output","w",stdout);
    ios::sync_with_stdio(false);
    int T,z,i,j,k,n,m;
    cin >> T;
    for (z = 1;z <= T;z++) {
    	cin >> R >> C;
    	vector<char> tmp(C);
    	M.clear();
    	M.resize(R,tmp);
    	for (i = 0;i < R;i++) {
    		for (j = 0;j < C;j++) {
    			cin >> M[i][j];
    		}
    	}
    	int ans = solve();
    	if (ans == -1) {
    		cout << "Case #" << z << ": IMPOSSIBLE" << endl;
    	}
    	else {
    		cout << "Case #" << z << ": " << ans << endl;
    	}
    }
    return 0;
}
