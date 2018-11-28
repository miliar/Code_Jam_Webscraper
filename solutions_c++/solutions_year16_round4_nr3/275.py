#pragma comment(linker, "/STACK:108777216")
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <deque>
#include <map>
#include <set>
#include <bitset>
#include <utility>
#include <algorithm>
using namespace std;

int const MAX_N = 1024;
int const MAX_CH = 100100;

int const UP = 1;
int const LEFT = 2;
int const RIGHT = 3;
int const DOWN = 4;

char st[MAX_CH];
char s[128][128];

int n,m,V;
int perm[100100];

int sm[1024][1024],sm_len[1024],sm_list[1024][1024];
int nnew[1024];

int get_index_by_XY(int x, int y, int DIR) {
	if (DIR == UP)
		return x*(m+m+1)+y;
	if (DIR == DOWN)
		return (x+1)*(m+m+1)+y;
	if (DIR == LEFT)
		return x*(m+m+1)+m+y;
	if (DIR == RIGHT)
		return x*(m+m+1)+m+y+1;
}

int get_vert_by_GG(int K) {
	if (K >= 0 && K < m)
		return get_index_by_XY(0,K,UP);
	if (K >= m && K < n+m)
		return get_index_by_XY(K-m, m-1, RIGHT);
	if (K >= n+m && K < n+m+m)
		return get_index_by_XY(n-1, m-1- (K-n-m), DOWN);

	return get_index_by_XY(n-1- (K-n-m-m), 0, LEFT);
}

void dfs(int V) {
	nnew[V] = 1;
	for (int i=0; i<sm_len[V]; i++)
		if (!nnew[sm_list[V][i]])
			dfs(sm_list[V][i]);
}

int shd[1024][1024];

int solve_slow(int cnt) {
	for (int i=0; i<cnt; i++)
		for (int j=0; j<cnt; j++)
			shd[i][j] = 0;

	for (int i=0; i<cnt; i+=2)
		shd[perm[i]][perm[i+1]] = shd[perm[i+1]][perm[i]] = 1;
	
	for (int code=0; code<(1<<(n*m)); code++) {
		int r = 0;
		for (int i=0; i<n; i++)
			for (int j=0; j<m; j++) {
				if ((code>>r)&1)
					s[i][j] = '/';
				else
					s[i][j] = '\\';
				r++;
			}
		V = n*(m+1)+m*(n+1);

		for (int i=0; i<V; i++)
			for (int j=0; j<V; j++)
				sm[i][j] = 0;

		for (int i=0; i<n; i++)
			for (int j=0; j<m; j++)
				if (s[i][j] == '/') {
					int v1 = get_index_by_XY(i,j,UP);
					int v2 = get_index_by_XY(i,j,LEFT);
					sm[v1][v2]=sm[v2][v1] = 1;

					v1 = get_index_by_XY(i,j,DOWN);
					v2 = get_index_by_XY(i,j,RIGHT);
					sm[v1][v2]=sm[v2][v1] = 1;
				}
				else {
					int v1 = get_index_by_XY(i,j,UP);
					int v2 = get_index_by_XY(i,j,RIGHT);
					sm[v1][v2]=sm[v2][v1] = 1;

					v1 = get_index_by_XY(i,j,DOWN);
					v2 = get_index_by_XY(i,j,LEFT);
					sm[v1][v2]=sm[v2][v1] = 1;
				}

		for (int i=0; i<V; i++) {
			sm_len[i] = 0;
			for (int j=0; j<V; j++)
				if (sm[i][j]) sm_list[i][sm_len[i]++] = j;
		}

		int Ok = 1;

		for (int i=0; i<cnt; i++) {
			for (int j=0; j<V; j++) nnew[j] = 0;
			int v_st = get_vert_by_GG(i);
			dfs(v_st);
			nnew[v_st] = 0;

			for (int j=0; j<cnt; j++) {
				int v_fn = get_vert_by_GG(j);
				if (shd[i][j] && !nnew[v_fn]) Ok = 0;
				else if (!shd[i][j] && nnew[v_fn]) Ok = 0;
			}
			
			if (!Ok) break;
		}

		if (Ok) {
			for (int i=0; i<n; i++) {
				printf("\n");
				for (int j=0; j<m; j++) printf("%c",s[i][j]);
			}
			return 1;
		}
	}

	return 0;
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	gets(st);
	int tst_count;
	sscanf(st,"%d",&tst_count);
	for (int qqq=1; qqq<=tst_count; qqq++) {
		cerr<<"\r"<<qqq<<"    ";

		if (qqq > 1) printf("\n");
		printf("Case #%d:",qqq);

		//
		cin>>n>>m;
		int cnt = (n+m)*2;
		for (int i=0; i<cnt; i++) {
			cin>>perm[i];
			perm[i]--;
		}

		if (!solve_slow(cnt)) printf("\nIMPOSSIBLE");
		//
	}
	return 0;
}