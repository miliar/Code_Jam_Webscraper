#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <queue>
#include <math.h>
#include <bitset>
#include <climits>
#define MP make_pair

using namespace std;
typedef long long LL;
typedef unsigned int uint;
const double pi = atan (1.0) * 4;

int R, C;
char ch[110][110];

bool is_imp (){
	for (int i=0;i<R;i++)	for (int j=0;j<C;j++) if (ch[i][j] != '.'){
		bool ok = true;
		for (int ii=0;ii<R;ii++)	if (ii != i)	if (ch[ii][j] != '.'){
			ok = false; break;
		}
		for (int jj=0;jj<C && ok;jj++) if (jj != j) if (ch[i][jj] != '.'){
			ok = false; break;
		}
		if (ok)	return true;
	}
	return false;
}
int get_ (char c){
	if (c == '^')	return 0;
	if (c == '>')	 return 1;
	if (c == 'v')	return 2;
	else	return 3;
	
}
int dr[4] = {-1,0,1,0};
int dc[4] = {0,1,0,-1};
bool is_in (int r, int c){
	return r>=0 && r<R && c>=0 && c<C;
}

int main (){
	int T; scanf ("%d",&T);
	for (int cas=1;cas<=T;cas++){
		scanf ("%d%d",&R,&C);
		for (int i=0;i<R;i++)	scanf ("%s",ch[i]);
		printf ("Case #%d: ", cas);
		if (is_imp())	printf ("IMPOSSIBLE\n");
		else{
			int ans = 0;
			for (int i=0;i<R;i++){
				for (int j=0;j<C;j++){
					if (ch[i][j] != '.'){
						int nd = get_ (ch[i][j]);
						int nr = i, nc = j;
						for (;;){
							nr += dr[nd];
							nc += dc[nd];
							if (!is_in(nr,nc))	break;
							if (ch[nr][nc] != '.')	break;
						}
						if (!is_in(nr,nc))	ans++;
					}
				}
			}
			printf ("%d\n", ans);
		}
	}
	return 0;
}