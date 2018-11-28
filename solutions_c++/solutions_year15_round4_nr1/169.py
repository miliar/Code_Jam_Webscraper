#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>

#define FOR(a,b,c) for (int c = (a), _for = (b); c < _for; ++c)
#define REP(n) for (int _rep = 0, _for = (n); _rep < _for; ++_rep)
#define pb push_back
#define x first
#define y second
#define ll long long
#define pii pair < int, int >

using namespace std;

int r, c;
char mat[105][105];
int cnt1[105], cnt2[105];

void Solve(){
	memset(mat, 0, sizeof mat);
	memset(cnt1, 0, sizeof cnt1);
	memset(cnt2, 0, sizeof cnt2);
	scanf("%d%d", &r, &c);
	FOR(0, r, i) scanf("%s", mat[i]);
	FOR(0, r, i) FOR(0, c, j) if (mat[i][j] != '.') ++cnt1[i], ++cnt2[j];
	FOR(0, r, i) FOR(0, c, j) if (mat[i][j] != '.') if (cnt1[i] == 1 && cnt2[j] == 1){printf("IMPOSSIBLE\n"); return;}
	int Sol = 0;
	FOR(0, r, i){
		if (!cnt1[i]) continue;
		int t = 0;
		do {
			if (mat[i][t] == '<') ++Sol;
		} while (mat[i][t++] == '.');
		t = c - 1;
		do {
			if (mat[i][t] == '>') ++Sol;
		} while (mat[i][t--] == '.');
	}
	FOR(0, c, i){
		if (!cnt2[i]) continue;
		int t = 0;
		do {
			if (mat[t][i] == '^') ++Sol;
		} while (mat[t++][i] == '.');
		t = r - 1;
		do {
			if (mat[t][i] == 'v') ++Sol;
		} while (mat[t--][i] == '.');
	}
	printf("%d\n", Sol);
}

int main(){
	int t;
	scanf("%d", &t);
	FOR(1, t + 1, i){
		printf("Case #%d: ", i);
		Solve();
	}                   
	return 0;          
}
