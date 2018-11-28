#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<cstring>
#include<set>
using namespace std;

typedef long long LL;

int N, M;
string S[8];
int cnt[1<<8];
int best;
set<vector<int> > ans;
int trie[9];


void rec(int p) {
    if (p==M) {
	int tmp = 0;
	for (int i=0; i<N; i++) tmp += cnt[trie[i]];

	if (tmp > best) {
	    ans.clear();
	    best = tmp;
	}
	if (tmp == best) {
	    ans.insert(vector<int>(trie, trie+N));
	}
	return ;
    }
    for (int i=0; i<N; i++) {
	trie[i] |= 1<<p;
	rec(p+1);
	trie[i] &= ~(1<<p);
    }
}

int main() {
    int T;
    scanf("%d", &T);

    for (int tc=1; tc<=T; tc++) {
	memset(cnt, 0, sizeof cnt);
	memset(trie, 0, sizeof trie);
	ans.clear(); best = 0;

	scanf("%d%d", &M, &N);
	for (int i=0; i<M; i++) cin >> S[i];

	for (int X=1; X<(1<<M); X++) {
	    set<string> se;
	    se.insert("");
	    for (int i=0; i<M; i++) {
		if (~X & (1<<i)) continue;
		for (int j=0; j<=(int)S[i].size(); j++)
		    se.insert(S[i].substr(0, j));
	    }
	    cnt[X] = se.size();
	}
	cnt[0] = -999999;

	best = 0;
	rec(0);
	
	printf("Case #%d: %d %d\n", tc, best, ans.size());
	
    }
    return 0;
}
