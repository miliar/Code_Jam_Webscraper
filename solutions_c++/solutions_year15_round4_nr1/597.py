//Author: net12k44
#include <bits/stdc++.h>
using namespace std;

const int limit = 200 + 5;
char a[limit][limit];
int dx[] = {1,-1,0,0};
int dy[] = {0,0,1,-1};
char c[] = {'v','^','>','<'};
int m, n;
const int inf = 1000000000;

bool valid(int i, int j){
	return 0<=i && i<m && 0<=j && j<n;
}

void solve(){
	scanf("%d%d\n",&m,&n);
	for(int i = 0; i < m; ++i) scanf("%s",a[i]);
 
	int res = 0;
	for(int i = 0; i < m; ++i)
	for(int j = 0; j < n; ++j)
		if (a[i][j] != '.'){
			int ok = 0;
			int deg = 0;
			for(int k = 0; k < 4; ++k){
				int ii = i+dx[k], jj = j+dy[k];
				while(valid(ii,jj) && a[ii][jj]=='.'){
					ii+=dx[k];
					jj+=dy[k];
				}
				if (valid(ii,jj)) {
					deg++;
					if (a[i][j] == c[k]) ok = 1;
				}
			}
			if (ok == 0){
				if (deg > 0) res++;
				else res = -inf;
			}
		}		
	

	if (res < 0) printf("IMPOSSIBLE\n");
	else printf("%d\n",res);

}

int main(){
	int test; scanf("%d\n",&test);
	for(int t = 1; t<=test; ++t){
		printf("Case #%d: ", t);
		solve();
	}
}
