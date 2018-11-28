
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

typedef long long i8;

int tst, n, m;
char str[101][101];
char cno[101];
vector<int> cnt[101];

int iab(int x) {
	return x<0?-x:x;
}

int opt(int j) {
	int re=999888777;
	for (int s=1; s<=100; s++) {
		int tr=0;
		for (int i=0; i<cnt[j].size(); i++) {
			tr+=iab(s-cnt[j][i]);
		}
		re=min(re,tr);
	}
	return re;
}

void solve() {
	m=0;
	for (int i=0; i<100; i++)
		cnt[i].clear();

	int p=0;
	while (str[0][p]) {
		char x=str[0][p];
		int c=1;
		while (str[0][++p]==x) 
			c++;
		cno[m]=x;
		cnt[m++].push_back(c);
	}
	cno[m]=0;
//printf(" '%s' ", cno);
	
	for (int i=1; i<n; i++) {
		int p=0, j=0;
//printf(" --------- i=%d str=%s\n", i, str[i]);
		while (str[i][p]) {
			char x=str[i][p];
			int c=1;
			while (str[i][++p]==x) 
				c++;
//printf(" p=%d x=%c c=%d\n", p, x, c);
			if (x!=cno[j]) {
				printf("Fegla Won\n");
				return;
			}
			cnt[j++].push_back(c);
		}
		if (j!=m) {
			printf("Fegla Won\n");
			return;
		}
	}
	
	int re=0;
	for (int i=0; i<m; i++)
		re += opt(i);
	printf("%d\n", re);
}

main() {
	scanf("%d", &tst);
	for (int cas=1; cas<=tst; cas++) {
		scanf("%d", &n);
		for (int i=0; i<n; i++)
			scanf("%s", str[i]);
		printf("Case #%d: ", cas);
		solve();
	}
}
