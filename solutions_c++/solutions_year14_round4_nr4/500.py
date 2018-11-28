#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
#define LL long long

int T[10],tt[10][100],next[10][100][50];

int n,m,x[10],best = 0,bcnt;
char s[100][105];

void add(int at,int tx,char *t) {
    if (t[0] == 0) {
        return;
    }
    int to = t[0]-'A';
    if (next[tx][at][to] == -1) {
		next[tx][at][to] = ++T[tx];
    }
    add(next[tx][at][to],tx,t+1);
}

void recur(int at) {
	if (at == n) {
		memset(tt,0,sizeof(tt));
		memset(next,-1,sizeof(next));
		memset(T,0,sizeof(T));
		/*
		for (int i=0; i<n; i++)
			printf("%d ",x[i]);
		puts("");
		*/
		for (int i=0; i<n; i++)
			add(0,x[i],s[i]);
		int ans = 0;
		for (int i=0; i<m; i++) {
			if (T[i] > 0) ans += T[i]+1;
			//printf("%d ",T[i]);
		}
		//printf(" = %d",ans);
		//puts("");
		if (ans > best) {
			best = ans;
			bcnt = 0;
		}
		if (ans == best) bcnt++;
		return;
	}
	for (int i=0; i<m; i++) {
		x[at] = i;
		recur(at+1);
	}
}

int main() {
	int tc;
    scanf("%d",&tc);
    for (int t=1; t<=tc; t++) {
    	scanf("%d%d",&n,&m);
    	best = 0;
    	for (int i=0; i<n; i++) {
			scanf("%s",s[i]);
    	}
    	recur(0);
    	printf("Case #%d: %d %d\n",t,best,bcnt);
    	fflush(stdout);
    }
	return 0;
}
