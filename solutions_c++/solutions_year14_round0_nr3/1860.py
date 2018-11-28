#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

const int MaxN = 15;
const int dr [] = {1, -1, 1, -1, 1, -1, 0, 0};
const int dc [] = {1, -1, -1, 1, 0, 0, 1, -1};

int R, C, M, a[MaxN][MaxN], tot, cookie, bio[MaxN][MaxN];

int count (int r, int c) {
  int ret = 0;
  for (int i = 0; i < 8; ++i) {
    int nr = r + dr[i], nc = c + dc[i];
    if (nr < 0 || nr >= R) continue;
    if (nc < 0 || nc >= C) continue;
    ret += a[nr][nc];
  }
  return ret;
}

void dfs (int r, int c) {
  ++tot;
  bio[r][c] = cookie;
  
  if (count(r, c) > 0)
    return;

  for (int i = 0; i < 8; ++i) { 
    int nr = r + dr[i], nc = c + dc[i];
    if (nr < 0 || nr >= R) continue;
    if (nc < 0 || nc >= C) continue;
    if (bio[nr][nc] != cookie)
      dfs(nr, nc);
  }
}

void solve (int tc) {
  scanf("%d %d %d",&R,&C,&M);
  for (int mask = 0; mask < (1 << (R * C)); ++mask) {
    if (__builtin_popcount(mask) != M)
      continue;
    
    for (int r = 0; r < R; ++r)
      for (int c = 0; c < C; ++c)
	a[r][c] = (mask & (1 << (r * C + c))) != 0 ? 1 : 0;

    for (int r0 = 0; r0 < R; ++r0)
      for (int c0 = 0; c0 < C; ++c0)
	if (!a[r0][c0]) {
	  ++cookie;
	  tot = 0;
	  dfs(r0, c0);
	  
	  if (tot == R * C - M) {
	    printf("Case #%d:\n",tc);
	    for (int r = 0; r < R; ++r, puts(""))
	      for (int c = 0; c < C; ++c) {
		if (r == r0 && c == c0)
		  printf("%c",'c');
		else
		  printf("%c",a[r][c] ? '*' : '.');
	      }
	    return;
	  }
	}
  }

  printf("Case #%d:\n",tc);
  printf("Impossible\n");
}

int main (void) {
  int t;
  scanf("%d",&t);
  for (int c = 1; c <= t; ++c)
    solve(c);
  return 0;
}
