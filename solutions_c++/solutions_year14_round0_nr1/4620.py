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

using namespace std;

template<class T> T abs(T x){if (x < 0) return -x; else return x;}

bool b[100];
int c[100][100];

int main(){
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int Cases = 1; Cases <= T; ++Cases){
		printf("Case #%d: ", Cases);
		memset(b, false, sizeof(b));
		int x;
		scanf("%d", &x);
		for (int i = 1; i <= 4; ++i)
			for (int j = 1; j <= 4; ++j)
				scanf("%d", &c[i][j]);
		for (int i = 1; i <= 4; ++i)
			b[c[x][i]] = true;
		int tot = 0, ans = 0;
		scanf("%d", &x);
		for (int i = 1; i <= 4; ++i)
			for (int j = 1; j <= 4; ++j)
				scanf("%d", &c[i][j]);
		for (int i = 1; i <= 4; ++i)
			if (b[c[x][i]]){
				++tot;
				ans = c[x][i];
			}
		if (tot == 1) printf("%d\n", ans); else 
			if (tot == 0) puts("Volunteer cheated!"); else 
				puts("Bad magician!");
	}
	return 0;
}

