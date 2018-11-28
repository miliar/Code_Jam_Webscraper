#include<iostream>
#include<string>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<ctime>
#include<algorithm>
#include<map>
using namespace std;

struct node { int nxt[26]; };
#define N 210
#define M 20
node trie[N];
int a[M], b[M];
int n, m, cnt;
char s[M][M];

void insert(int x, int y) {
	++cnt; memset(trie[cnt].nxt, 0, sizeof(trie[cnt].nxt));
	trie[x].nxt[y]=cnt;
}

void trie_input(int id, char *str) {
	if (str[0]=='\0') return;
	if (!trie[id].nxt[str[0]-'A']) insert(id, str[0]-'A');
	trie_input(trie[id].nxt[str[0]-'A'], str+1);
}

int cal(int x) {
	int i;
	cnt=1; memset(trie[1].nxt, 0, sizeof(trie[1].nxt));
	for (i=0; i<n; ++i) if (a[i]==x) trie_input(1, s[i]);
	return cnt;
}

void conduct() {
	int i, j, ans, tmp, tmp2, cum;
	scanf("%d%d", &n, &m);
	for (i=0; i<n; ++i) scanf("%s", s[i]);
	for (b[0]=1, i=1; i<=n; ++i) b[i]=b[i-1]*m;
	for (ans=0, cum=0, i=0; i<b[n]; ++i) {
		for (j=0; j<n; ++j) a[j]=i/b[j]%m;
		for (tmp=j=0; j<m; ++j) {
			tmp2=cal(j);
			if (tmp2==1) break;
			tmp+=tmp2;
		}
		if (j<m) continue;
		if (tmp>ans) { ans=tmp; cum=0; }
		if (tmp==ans) cum++;
	}
	printf("%d %d\n", ans, cum);
}

int main() {
	int time; scanf("%d", &time);
	for (int i=1; i<=time; ++i) {
		printf("Case #%d: ", i);
		conduct();
	}
	return 0;
}
