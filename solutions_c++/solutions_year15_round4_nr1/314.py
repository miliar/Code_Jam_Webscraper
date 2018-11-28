#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;
#define FOR(i,j,k) for(i=j;i<=k;++i)
#define MET(i,j) memset(i,j,sizeof(i))
#define FORD(i,j,k) for(i=j;i>=k;--i)
#define N 105
char map[N][N];
int left[N][N],right[N][N],up[N][N],down[N][N];

int main() {
	//freopen("a.in","r",stdin);
	int T,i,j,k,r,c,ans;
	scanf("%d",&T);
	FOR(k,1,T) {
		scanf("%d %d\n",&r,&c);
		MET(map,0);
		FOR(i,1,r) {
			FOR(j,1,c) {
				map[i][j] = getchar();
			}
			getchar();
		}
		MET(left,0);
		MET(right,0);
		MET(up,0);
		MET(down,0);
		FOR(i,1,r) {
			FOR(j,1,c) {
				if(map[i][j]!='.') {
					left[i][j]=1;
					break;
				}
			}
			FORD(j,c,1) {
				if(map[i][j]!='.') {
					right[i][j]=1;
					break;
				}
			}
		}
		FOR(j,1,c) {
			FOR(i,1,r) {
				if(map[i][j]!='.') {
					up[i][j]=1;
					break;
				}
			}
			FORD(i,r,1) {
				if(map[i][j]!='.') {
					down[i][j]=1;
					break;
				}
			}
		}
		bool flag = 1;
		FOR(i,1,r){
			FOR(j,1,c) {
				if(left[i][j] + right[i][j] + up[i][j] + down[i][j] == 4) {
					flag = 0;
					break;
				}
			}
			if(!flag) break;
		}
		if(flag) {
			ans = 0;
			FOR(i,1,r) {
				FOR(j,1,c){
					if(map[i][j]=='<' && left[i][j]) ans++;
					if(map[i][j]=='>' && right[i][j]) ans++;
					if(map[i][j]=='^' && up[i][j]) ans++;
					if(map[i][j]=='v' && down[i][j]) ans++;
				}
			}
			printf("Case #%d: %d\n",k,ans);
		} else {
			printf("Case #%d: IMPOSSIBLE\n",k);
		}
	}
}