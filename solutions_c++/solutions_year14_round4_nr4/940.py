#include <cstdio>
#include <vector>
#include <algorithm>
#include <string.h>
#define M 1010
#define N 110
#define S 110

using namespace std;

char s[M][S];
int  mx, cnt, n, m, ad;
vector<int> set[N];

struct trie{
	trie* l[26];
	trie(){
		memset(l, 0, sizeof(trie*) * 26);
	}
}*root;

	void clear(trie* n){
		for (int i = 0; i < 26; i++)
			if (n->l[i] != NULL)
				clear(n->l[i]);
		delete n;
	}
void add(char *s){
	trie* p = root;
	for (; *s; ++s){
		if (!p->l[*s-'A']){
			p->l[*s-'A'] = new trie();
			ad++;
		}
		p = p->l[*s-'A'];
	}
}

void check(){
	for (int i = ad = 0; i < n; i++){
		root = new trie();
		for (int j = 0; j < set[i].size(); j++)
			add(s[set[i][j]]);
		clear(root);
	}
}

void DFS(int now){
	if (now == m){
		for (int i = 0; i < n; i++)
			if (set[i].size() == 0)
				return;
		check();
		if (mx < ad){
			cnt = 1;
			mx = ad;
		}
		else if (mx == ad)
			cnt++;
		return;
	}
	for (int i = 0; i < n; i++){
		set[i].push_back(now);
		DFS(now+1);
		set[i].pop_back();
	}
}

int main(){
	int T, cas, i;
	scanf("%d", &T);
	for (cas = 1; cas <= T; cas++){
		scanf("%d %d", &m, &n);
		for (i = 0; i < m; i++)
			scanf("%s", s[i]);
		for (i = 0; i < n; i++)
			set[i].clear();
		mx = 0;
		DFS(0);
		printf("Case #%d: %d %d\n", cas, mx+n, cnt);
	}
}

