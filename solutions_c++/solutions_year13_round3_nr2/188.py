
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

typedef long long i8;

int tst;
char bm[1600][1600];
int cnt[1600][1600];

void mark(int x, int y, char d, vector<int> &v, int m) {
	if (x>=0 && x<1600 && y>=0 && y<1600 && !bm[x][y]) {
		bm[x][y]=d;
		cnt[x][y]=m;
		v.push_back(x);
		v.push_back(y);
	}
}

void init() {
	int x=800,y=800;
	bm[x][y]='t';
	vector<int> a[2];
	a[1].push_back(x); a[1].push_back(y);
	for (int m=1; m<502; m++) {
		vector<int> &c=a[m%2], &f=a[(m+1)%2];
		f.clear();
		for (int i=0; i<c.size(); i+=2) {
			x=c[i]; y=c[i+1];
			mark(x+m,y,'E',f,m);
			mark(x-m,y,'W',f,m);
			mark(x,y+m,'N',f,m);
			mark(x,y-m,'S',f,m);
		}
	}
}

char re[505];
void solve(int x, int y) {
	x+=800; y+=800;
	int sz=0;
	while (bm[x][y]!='t') {
		char z=bm[x][y];
		re[sz++]=z;
		int m=cnt[x][y];
		switch (z) {
		case 'N': y-=m; break;
		case 'S': y+=m; break;
		case 'E': x-=m; break;
		case 'W': x+=m; break;
		}
	}
	reverse(re,re+sz);
	re[sz]=0;
}

main() {
	init();

	scanf("%d", &tst);
	for (int cas=1; cas<=tst; cas++) {
		int x, y;
		scanf("%d%d",&x,&y);
		solve(x,y);
		printf("Case #%d: %s\n", cas, re);
	}
}
