#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cassert>
using namespace std;
typedef long long ll;
typedef double R;
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define FOR(i, s, t) for(i = (s); i < (t); i++)
#define RFOR(i, s, t) for(i = (s)-1; i >= (t); i--)

const int MAXN = 2091;

int min(int a, int b, int c){
	return min(a, min(b, c));
}

int max(int a, int b, int c){
	return max(a, max(b, c));
}

int ans[15][3][3] = {1, 0, 0, 0, 1, 0, 0, 0, 1};

void solve(int n, int j){
	if(n == 0){
		char s[] = "PRS";
		printf("%c", s[j]);
	}
	else{
		int y, z;
		if(j == 0){
			y = 0;
			z = 1;
		}
		else if(j == 1){
			y = 0;
			z = 2;
		}
		else{
			y = 1;
			z = 2;
		}
		solve(n-1, y);
		solve(n-1, z);
	}
}

int main(){
#ifdef LOCAL
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
#endif
	int T, i0;
	scanf("%d", &T);
	for(i0 = 1; i0 <= T; i0++){
		int n;
		int p, r, s;
		scanf("%d%d%d%d", &n, &r, &p, &s);
		printf("Case #%d: ", i0);
		if(max(p, r, s) - min(p, r, s) > 1)
			puts("IMPOSSIBLE");
		else{
			for(int i = 0; i < 13; i++){
				int x, y, z;
				x = 0;
				y = 0;
				z = 1;
				ans[i+1][x][0] = ans[i][y][0] + ans[i][z][0];
				ans[i+1][x][1] = ans[i][y][1] + ans[i][z][1];
				ans[i+1][x][2] = ans[i][y][2] + ans[i][z][2];
				x = 1;
				y = 0;
				z = 2;
				ans[i+1][x][0] = ans[i][y][0] + ans[i][z][0];
				ans[i+1][x][1] = ans[i][y][1] + ans[i][z][1];
				ans[i+1][x][2] = ans[i][y][2] + ans[i][z][2];
				x = 2;
				y = 1;
				z = 2;
				ans[i+1][x][0] = ans[i][y][0] + ans[i][z][0];
				ans[i+1][x][1] = ans[i][y][1] + ans[i][z][1];
				ans[i+1][x][2] = ans[i][y][2] + ans[i][z][2];
			}
			for(int j = 0; j < 3; j++)
				if(ans[n][j][0] == p && ans[n][j][1] == r && ans[n][j][2] == s)
					solve(n, j);
			puts("");
		}
	}
	return 0;
}
