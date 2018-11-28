#include <cstdio>
#include <cstdlib>
#include <map>
#include <queue>
#include <cstring>
#include <string>
#include <cctype>
#include <algorithm>
#include <cmath>
#include <set>

using namespace std;
typedef long long ll;

int n, t, r, c, m;
map<ll, int> cache;
bool grid[5][5];
bool grid2[5][5];
char ans[5][6];
int ra[5] = {1, 1, 1, 0, -1};
int rb[5] = {-1, 0, 1, 1, 1};

ll convert(int left) {
	ll res = left << 3;
	res += r;
	res <<= 3;
	res += c;
	for(int i = 0; i < 5; ++i)
		for(int j = 0; j < 5; ++j){
			res <<= 1;
			res += grid[i][j];
		}	
	return res;
}

int click(int a, int b){
	if(a == r || b == c || a < 0 || b < 0) return 0;
	if(grid2[a][b]) return 0;
	grid2[a][b] = true;
	for(int i = 0; i < 5; ++i){
		int aa = a + ra[i];
		int bb = b + rb[i];
		if (aa < 0 || aa == r) continue;
		if (bb < 0 || bb == c) continue;
		if (grid[aa][bb]) return 1;
	}
	return 1 + click(a+1,b) + click(a,b+1) + click(a+1,b+1);
}
void printgrid(int z){
	memset(ans, 0, sizeof ans);
	for(int i = 4; i >= 0; --i){
		for(int j = 4; j >= 0; --j){
			if(i < r && j < c) {
				ans[i][j] = (z&1) ? '*' : '.';
			}
			z >>= 1;
		}
	}
	ans[0][0] = 'c';
	for(int i = 0; i < r; ++i)
		printf("%s\n", ans[i]);
}

int go(int i, int j, int left) {
	if (j == c) {
		i++;
		j = 0;
	}
	if(left > c-j + (r-i-1)*c) return -1;
	ll at = convert(left);
	int answer = cache[at];
	if (answer) return answer;
	if(!left) {
		memset(grid2, 0, 25);
		if(click(0,0) == m) return cache[at] = at&0x1FFFFFF;
		return cache[at] = -1;
	}
	grid[i][j] = 0;
	int res = go(i,j+1,left-1);
	grid[i][j] = 1;
	if (res > -1) return cache[at]=res;
	return cache[at] = go(i,j+1,left);
}

int main () {
	scanf("%d", &t);
	for (int _ = 1; _ <= t; _++){
		printf("Case #%d:\n", _);
		scanf("%d %d %d", &r, &c, &m);
		memset(grid, 1, 25);
		m = r*c-m;
		grid[0][0] = 0;
		int z;
		if((z=go(0,1,m-1)) > -1) printgrid(z);
		else printf("Impossible\n");
	}
return 0;
}