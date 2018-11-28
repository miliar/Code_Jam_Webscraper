#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
#include <cstdlib>
#define FOR(i,s,e) for (int i=(s); i<(e); i++)
#define FOE(i,s,e) for (int i=(s); i<=(e); i++)
#define FOD(i,s,e) for (int i=(s)-1; i>=(e); i--)
#define CLR(a,x) memset(a, x, sizeof(a))
#define EXP(i,l) for (int i=(l); i; i=qn[i])
#define LLD long long
using namespace std;

int n, m;
int a[202][1005];
int l[202];
map<string, int> D;
char s[20005], ss[20];
int v[20005][2];
int id[205], ret;

int mapto(char s[]){
	string ss = (string)s;
	if (D[s] != 0) return D[s];
	D[s] = ++m;
	return m;
}

void update(int x, int id){
	FOR(i,0,l[x]){
		v[a[x][i]][id]++;
		if (v[a[x][i]][id] == 1 && v[a[x][i]][id^1]) ++ret;
	}
}

void remove(int x, int id){
	FOR(i,0,l[x]){
		v[a[x][i]][id]--;
		if (v[a[x][i]][id] == 0 && v[a[x][i]][id^1]) --ret;
	}
}

void solve(int tc){
	m = 0;
	scanf("%d", &n); gets(s);
	D.clear();
	FOR(i,0,n){
		l[i] = 0;
		gets(s);
		for (char *c = strtok(s, " "); c != NULL; c = strtok(NULL, " ")){
			sscanf(c, "%s", &ss);
			a[i][l[i]++] = mapto(ss);
		}
	}
	
	int rett = m;
	FOR(itr,0,20000){
		ret = 0;
		FOE(i,0,m) v[i][0] = v[i][1] = 0;

		FOR(i,0,2){
			FOR(k,0,l[i]) v[a[i][k]][i] = 1;
		}
		FOE(i,1,m){
			if (v[i][0] && v[i][1]) ++ret;
		}
		
		FOR(i,2,n){
			id[i] = rand() % 2;
			update(i, id[i]);		
		}
		
		while (1){
			int ok = 0;
			FOR(i,2,n){
				int cur = ret;
				remove(i, id[i]);
				id[i] ^= 1;
				update(i, id[i]);
				if (ret < cur){
					ok = 1;
				}
				else{
					remove(i, id[i]);
					id[i] ^= 1;
					update(i, id[i]);
				}
			}
			if (!ok) break;
		}
		rett = min(rett, ret);
	}

	printf("Case #%d: %d\n", tc, rett);
	fprintf(stderr, "Case #%d: %d\n", tc, rett);
}

int main(){
	srand(2134);
	int tc;
	scanf("%d", &tc);
	FOE(i,1,tc) solve(i);
	return 0;
}
