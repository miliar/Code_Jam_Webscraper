#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cstdlib>
#include<cmath>
#include<cctype>
#include<ctime>
#include<algorithm>
#include<iomanip>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<cassert>
#include<bitset>

using namespace std;

const int N = 100, M = 20000;

int a[200], b[200];
int to[M], last[N], nxt[M], tot = 0;
int view[N];

void add1(int x, int y){
	nxt[tot] = last[x];
	to[tot] = y;
	last[x] = tot;
	tot++;
}

void add(int x, int y){
	add1(x, y);
	add1(y, x);
}

void dfs(int x){
	view[x] = 1;
	int ed = last[x];
	while(ed != -1){
		if(!view[to[ed]]){
			dfs(to[ed]);
		}
		ed = nxt[ed];
	}
}

int check(int x, int y){
	memset(view, 0, sizeof(view));
	dfs(x);
	if(view[y]) return 1;
	return 0;
}
int main() {
	int TT;
	scanf("%d", &TT);
	for(int cc = 1; cc <= TT; cc++){
		printf("Case #%d:\n", cc);
		int r, c;
		scanf("%d%d", &r, &c);
		for(int i = 0; i < c; ++i){
			b[i] = i * 4;
		}
		for(int i = c; i < r + c; ++i){
			b[i] = 4 * c * (i - c) + 1 + (c - 1) * 4;
		}
		b[r + c] = b[r + c - 1] + 1;
		for(int i = r + c + 1; i < c + r + c; i++){
			b[i] = b[i - 1] - 4;
		}
		b[c + r + c] = b[c + r + c - 1] + 1;
		for(int i = c + r + c + 1; i < c + c + r + r; i ++){
			b[i] = b[i - 1] - 4 * c;
		}
		for(int i = 0; i < 2 * (r + c); i++){
			scanf("%d", a + i);
			a[i] = b[a[i] - 1];
		}
		int ok = 0;
		int up = 1 << (r * c);
		for(int t = 0; t < up; t++){
			tot = 0;
			memset(last, -1, sizeof(last));
			for(int i = 0; i < r; ++i){
				for(int j = 0; j < c - 1; j++){
					add(4 * (i * c + j)+ 1, 4 *(i * c + j + 1) + 3);
				}
			}
			for(int i = 0; i < r - 1; ++i){
				for(int j = 0; j < c; ++j){
					add(4 * (i * c + j)+ 2, 4 * ((i + 1) * c + j)+ 0);
				}
			}
			for(int i = 0; i < r; ++i){
				for(int j =0; j < c; ++j){
					if((1<<(i * c + j)) & t){
						add(4 * (i * c + j) , 4 * (i * c + j) + 1);
						add(4 * (i * c + j) + 2 , 4 * (i * c + j) + 3);
					}
					else {
						add(4 * (i * c + j) , 4 * (i * c + j) + 3);
						add(4 * (i * c + j) + 1, 4 * (i * c + j) + 2);
					}
				}
			}
			int flag = 1;
			for(int i = 0; i < r + c; ++i){
				if(!check(a[i * 2], a[i * 2 + 1])) flag = 0;
			}
			if(flag) {
				for(int i = 0; i < r; ++i){
					for(int j = 0; j < c; ++j){
						if((1<<(i * c + j)) & t)printf("\\");
						else printf("/");
					}
					printf("\n");
				}
				ok = 1;
				break;
			}
		}
		if(ok == 0) printf("IMPOSSIBLE\n");
	}
	return 0;
}

