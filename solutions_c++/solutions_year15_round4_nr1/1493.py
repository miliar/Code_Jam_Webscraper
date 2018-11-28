#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
const int MAXL = 103;
int a[MAXL][MAXL],b[MAXL][MAXL],n,m,ret;
char map[MAXL][MAXL];

int main(){
	int TT;
	freopen("input","r",stdin);
	freopen("output","w",stdout);
	scanf("%d",&TT);
	for(int Cas = 1;Cas <= TT;++ Cas){
		printf("Case #%d: ",Cas);
		scanf("%d%d",&n,&m);
		memset(a,0,sizeof(a)); memset(b,0,sizeof(b));
		for(int i = 0;i < n;++ i) scanf("%s",map[i]);
		for(int i = 0;i < n;++ i){
			for(int j = 0,sum = 0;j < m;++ j){
				b[i][j] |= sum;
				if(map[i][j] == '<') a[i][j] |= sum;
				if(map[i][j] != '.') sum = 1;
			}
			for(int j = m - 1,sum = 0;j >= 0;-- j){
				b[i][j] |= sum;
				if(map[i][j] == '>') a[i][j] |= sum;
				if(map[i][j] != '.') sum = 1;
			}
		}
		for(int j = 0;j < m;++ j){
			for(int sum = 0,i = 0;i < n;++ i){
				b[i][j] |= sum;
				if(map[i][j] == '^') a[i][j] |= sum;
				if(map[i][j] != '.') sum = 1;
			}
			for(int sum = 0,i = n - 1;i >= 0;-- i){
				b[i][j] |= sum;
				if(map[i][j] == 'v') a[i][j] |= sum;
				if(map[i][j] != '.') sum = 1;
			}
		}
		bool flag = true;
		ret = 0;
		for(int i = 0;i < n;++ i)
			for(int j = 0;j < m;++ j)
			if(map[i][j] != '.' && !a[i][j]){
				if(!b[i][j]){
					flag = false; j = m; i = n; continue;
				}
				++ ret;
			}
		if(flag)
			printf("%d\n",ret);
		else puts("IMPOSSIBLE");
	}
	return 0;
}
