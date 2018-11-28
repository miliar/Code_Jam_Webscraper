#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<queue>
#define FI(i,a, b) for(int i=a;i<=b;i++)
#define FD(i,a, b) for(int i=a;i>=b;i--)

#define CL(x, y) memset(x, y, sizeof(x))
#define INF 2000000000
#define MAXN ?
#define MAXE ?
#define ll long long
using namespace std;
int n, m, r, c, T;
char s[105][105];
int dx[1000], dy[1000];
int check(char dir, int x, int y){
	int da = dx[dir], db = dy[dir], a = x, b = y;
	while(s[a][b]){
		a += da, b += db;
		if(s[a][b] && s[a][b] != '.') return 1;
	}
	return 0;
}
int main(){
	dx['^'] = -1, dy['^'] = 0;
	dx['v'] = 1, dy['v'] = 0;
	dx['>'] = 0, dy['>'] = 1;
	dx['<'] = 0, dy['<'] = -1;
	scanf("%d", &T);
	FI(k, 1, T){
		CL(s, 0);
		int ans = 0, imp = 0;
		scanf("%d%d", &r, &c);
		printf("Case #%d: ", k);
		FI(i, 1, r) scanf("%s", s[i] + 1);
		FI(i, 1, r) FI(j, 1, c){
			if(s[i][j] != '.'){
				if(!check('^', i, j) && !check('v', i, j) && !check('>', i, j) && !check('<', i, j))
					imp = 1;
				else if(!check(s[i][j], i, j))
					ans++;
			}
		}
		if(imp) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}
}
