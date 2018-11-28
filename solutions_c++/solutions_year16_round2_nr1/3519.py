#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <bitset>

typedef long long LL;
#define pb push_back
#define MPII make_pair<int, int>
#define PII pair<int, int>
#define sz(x) (int)x.size()
#define fix(x) x - 'A'

using namespace std;

template<class T> T abs(T x){if (x < 0) return -x; else return x;}

char buf[2010];
int s[30];
int cnm[20][30];
bool ok;

void add(int idx, char *str){
	int len = strlen(str);
	for (int i = 0; i < len; ++i) ++cnm[idx][fix(str[i])];
}

void dfs(int st, int now){
	if (now == 0){
		ok = true;
		return;
	}
	for (int u = st; u >= 0; --u){
		bool f = true;
		int tmp = 0;
		for (int i = 0; i < 26; ++i){
			if (s[i] < cnm[u][i]){
				f = false;
				break;
			}
			tmp += cnm[u][i];
		}
		if (!f) continue;
		for (int i = 0; i < 26; ++i)
			s[i] -= cnm[u][i];
		dfs(u, now - tmp);
		if (ok){
			printf("%d", u);
			return;
		}
		for (int i = 0; i < 26; ++i)
			s[i] += cnm[u][i];
	}
}

int main(){
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	memset(cnm, 0, sizeof(cnm));
	add(0, "ZERO");
	add(1, "ONE");
	add(2, "TWO");
	add(3, "THREE");
	add(4, "FOUR");
	add(5, "FIVE");
	add(6, "SIX");
	add(7, "SEVEN");
	add(8, "EIGHT");
	add(9, "NINE");
	int cases;
	scanf("%d", &cases);
	for (int cc = 1; cc <= cases; ++cc){
		printf("Case #%d: ", cc);
		scanf("%s", buf);
		int len = strlen(buf);
		memset(s, 0, sizeof(s));
		for (int i = 0; i < len; ++i){
			++s[fix(buf[i])];
		}
		ok = false;
		dfs(9, len);
		printf("\n");
	}
	return 0;
}

