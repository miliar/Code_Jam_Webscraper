#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <string>
#include <climits>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>
#include <ctime>
#include <iostream>

#define PI 3.14159265358979
#define EPS 1e-9

using namespace std;

#define REP(i, n) for (int i=0; i<n; i++)
#define FOR(i, m, n) for (int i=m; i<=n; i++)
#define ABS(a) (((a)>0)?(a):(-(a)))
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> ii;

int CNT;

struct Trie {
    bool konec;
    struct Trie *dalsi[26];
};
void trie_free(Trie *t) {
    if (t==NULL) return;
    REP(i, 26) trie_free(t->dalsi[i]);
    free(t);
    t = NULL;
}
Trie* create() {
	CNT++;
    Trie *t = (Trie*)malloc(sizeof(Trie));
    REP(i, 26) t->dalsi[i] = NULL;
     t->konec = false;
    return t;
}
bool find(Trie *t, char *s) {
    if (t==NULL) return false;
    while (*s!='\0') {
        if (t->dalsi[(*s)-'A']) {
            t = t->dalsi[(*s)-'A'];
        }
        else return false;
        s++;
    }
    if (t->konec) return true;
    return false;
}
void add(Trie *t, char *s) {
	while(*s!='\0') {
		if (t->dalsi[(*s)-'A']==NULL)
			t->dalsi[(*s)-'A'] = create();
		t = t->dalsi[(*s)-'A'];
		s++;
	}
	t->konec = true;
}

int n, m;
char s[10][111];
char kam[10];
int ans;
vector<int> sol;
Trie *tr[10];

void zkus_trie() {
	REP(i, n) tr[i] = NULL;
	CNT = 0;
	REP(i, m) {
		if (tr[kam[i]]==NULL) tr[kam[i]] = create();
		add(tr[kam[i]], s[i]);
	}
	sol.push_back(CNT);
	REP(i, n) {
		trie_free(tr[i]);
	}
}

void zkus(int k) {
	if (k==m) {
		zkus_trie();
	}
	else {
		REP(i, n) {
			kam[k] = i;
			zkus(k+1);
		}
	}
}

void solve() {
	scanf("%d%d", &m, &n);
	sol.clear();
	REP(i, m) {
		scanf(" %s", s[i]);
	}
	zkus(0);
	sort(sol.begin(), sol.end());
	int x = sol[sol.size()-1];
	int y = 1;
	int j = sol.size()-2;
	while (j>=0 && sol[j]==sol[j+1]) { j--; y++; }
	printf("%d %d\n", x, y);
}

int main() {
	int t; scanf("%d", &t);
	REP (i, t) {
		printf("Case #%d: ", i+1);
		solve();
	}
	return 0;
}
