#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;
const int N = 105;
typedef long long LL;

int mat[N][N], tmp[N][N], n, m;
void solve(){
	for (int i = 0; i < n; ++i){
		int rMax = 0;
		for (int j = 0; j < m; ++j)
			if (mat[i][j] > rMax)
				rMax = mat[i][j];
		for (int j = 0; j < m; ++j)
			if (tmp[i][j] > rMax)
				tmp[i][j] = rMax;
	}
	for (int i = 0; i < m; ++i){
		int cMax = 0;
		for (int j = 0; j < n; ++j)
			if (mat[j][i] > cMax)
				cMax = mat[j][i];
		for (int j = 0; j < n; ++j)
			if (tmp[j][i] > cMax)
				tmp[j][i] = cMax;
	}
}
bool judge(){
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
			if (mat[i][j] != tmp[i][j])
				return false;
	return true;
}
int main(){
	int T;
	scanf("%d", &T);
	for (int cs = 1; cs <= T; ++cs){
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				tmp[i][j] = 1000;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				scanf("%d", &mat[i][j]);
		solve();
		printf("Case #%d: ", cs);
		if (judge()) puts("YES");
		else puts("NO");
	}
	return 0;
}