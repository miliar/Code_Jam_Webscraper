#include<cstdio>
#include<iostream>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<vector>
#include<stack>
#include<queue>
#include<string>
#include<iomanip>
#include<fstream>
#include<ctime>
using namespace std;
typedef vector<int> VI;
typedef pair <int,int> ii;
typedef long long LL;
#define pb push_back
const int INF = 2147483647;

int z, q, r, c, tab[105][105],i,j,a,b,okk,sum, pos, k, res;
char t[105];
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

bool ok(int a, int b) {
	return a >= 0 && a < r && b >= 0 && b < c;	
}

int main() {
scanf("%d",&z);
for (q=1;q<=z;q++) {
	scanf("%d %d",&r,&c);
	for (i=0;i<r;i++) {
		scanf("%s",t);
		for (j=0;j<c;j++) {
			if (t[j]=='>') tab[i][j] = 0;
			else if (t[j]=='v') tab[i][j] = 1;
			else if (t[j]=='<') tab[i][j] = 2;
			else if (t[j]=='^') tab[i][j] = 3;
			else tab[i][j] = -1;
		}
	}
	res = 0;
	pos = 1;
	for (i=0;i<r;i++) for (j=0;j<c;j++) if (tab[i][j] != -1) {
		a = i;
		b = j;
		okk = 0;
		while (1) {
			a += dx[tab[i][j]];
			b += dy[tab[i][j]];
			if (!(ok(a,b))) {
				break;
			}
			if (tab[a][b] != -1) {
				okk = 1;
				break;
			}
		}
		//printf("%d %d %d\n",i,j,okk);
		if (!okk) {
			res++;
			sum = 0;
			for (k=0;k<4;k++) {
				a = i;
				b = j;
				okk = 0;
				while (1) {
					a += dx[k];
					b += dy[k];
					if (!(ok(a,b))) {
						break;
					}
					if (tab[a][b] != -1) {
						okk = 1;
						break;
					}
				}
				if (!okk) sum++;
			}
			if (sum == 4) pos = 0;
		}
	}
	if (pos == 0) {
		printf("Case #%d: IMPOSSIBLE\n", q);	
	} else {
		printf("Case #%d: %d\n", q, res);
	}
}
return 0;
}

