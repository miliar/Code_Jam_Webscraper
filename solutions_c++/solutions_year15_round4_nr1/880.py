#include <iostream>
#include <stack>
#include <set>
#include <map>
#include <queue>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <string>
#include <deque>
#include <cmath>
#include <iomanip>

using namespace std;

const int INF = 1000000007;
const int MOD = 1000000007;

const int N = 100007;

int main() {
	int T;
	cin>>T;
	map<char,int> m;
	m['>'] = 0;
	m['<'] = 1;
	m['v'] = 2;
	m['^'] = 3;
	for(int I=1;I<=T;++I) {
		int r,c;
		cin>>r>>c;
		vector<string> g;
		g.resize(r);
		for(int i=0;i<r;++i)cin>>g[i];
		int res = 0;
		for(int i=0;res>=0&&i<r;++i) {
			for(int j=0;res>=0&&j<c;++j) {
				int ok[4];
				memset(ok, 0, sizeof(ok));
				for(int k=j+1; k<c;++k) {
					if (g[i][k] != '.') {
						ok[0]++;
						break;
					}
				}
				for(int k=j-1;k>=0;--k) {
					if (g[i][k] != '.') {
						ok[1]++;
						break;
					}
				}
				for(int k=i+1;k<r;++k) {
					if (g[k][j] != '.') {
						ok[2]++;
					}
				}
				for(int k=i-1;k>=0;--k) {
					if (g[k][j] != '.') {
						ok[3]++;
					}
				}
				if (g[i][j] != '.' && ok[m[g[i][j]]] == 0) {
					bool all = true;
					for(int i=0;i<4;++i) {
						if (ok[i] > 0) all = false;
					}
					if (all) {
						res = -1;
					} else {
						res++;
					}
				}
			}
		}
		if (res < 0) {
			printf("Case #%d: IMPOSSIBLE\n", I);
		} else {
			printf("Case #%d: %d\n", I,res);
		}
	}
	return 0;
}
