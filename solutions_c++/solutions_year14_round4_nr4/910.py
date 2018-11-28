#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
using namespace std;
int m, n;
char str[100][100];
int belongs[10];
struct node {
	node * ch[26];
} pool[10*10*10], *buf = NULL, *head[10];
int cnt = 0;

void insert(node * cur, char * str){
	int l = strlen(str);
	for (int i = 0; i < l; i++)
		if (cur->ch[str[i] - 'A'] == NULL){
			cur->ch[str[i] - 'A'] = buf++;
			cnt++;
			cur = cur->ch[str[i] - 'A'];
		} else {
			cur = cur->ch[str[i] - 'A'];
		}
}

int maxLen, maxCnt;
bool hit[10];
void calc(){
	memset(pool, 0, sizeof(pool));
	buf = pool; cnt = 0;
	memset(hit,0,sizeof(hit));
	for (int i = 0; i < m; i++)
		hit[belongs[i]] = true;
	for (int i = 0; i < n; i++)
		if (!hit[i])
			return ;
	for (int i = 0; i < n; i++){
		head[i] = buf++;cnt++;
	}
	for (int i = 0; i < m; i++){
		insert(head[belongs[i]], str[i]);
	}
	if (maxLen < cnt)
		maxLen = cnt, maxCnt = 0;
	if (maxLen == cnt){
		maxCnt++;
		
	}
}
void dfs(int x){
	if (x == m){
		calc();
		return ;
	}
	for (int i = 0; i < n; i++){
		belongs[x] = i;
		dfs(x + 1);
	}

}
int main(){
	freopen("P3_small.in", "r", stdin);
	freopen("P3_small.out", "w", stdout);

	int T; scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++){
		fprintf(stderr, "%d\n", cas);
		printf("Case #%d: ", cas);
		scanf("%d%d", &m, &n);
		memset(str,0,sizeof(str));
		for (int i = 0; i < m; i++)
			scanf("%s", &str[i]);
		maxLen = maxCnt = 0;
		dfs(0);
		printf("%d %d\n", maxLen, maxCnt);
	}
}