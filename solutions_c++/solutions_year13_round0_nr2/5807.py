#include<iostream>
#include<map>
#include<string>
#include<algorithm>
#include<bitset>
#include<cassert>
#include<cstring>
#include<cmath>
#include<cstdio>
#include<queue>
#include<stack>
#include<vector>
#include<ctime>
#include<functional>
#include<set> 
#include<cctype>
#include<cstdlib>
using namespace std;
const double eps=1e-7;
const int BASE = 64;
const int maxn = BASE + 256;
const int maxe = BASE + 100;
const int INF = (1<<30)-1;
typedef unsigned long long ULL;
int bd[16][16];
int row[2][16],col[2][16],n,m;
int main(){
	//freopen("B-small-attempt0.in","r",stdin);
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int cs = 1; cs <= T; ++cs){
		printf("Case #%d: ",cs);
		for(int i = 0; i < 10; ++i){
			row[0][i] = 0;
			row[1][i] = INF;
			col[0][i] = 0;
			col[1][i] = INF;
		}
		scanf("%d%d",&n,&m);
		for(int i = 0; i < n; ++i){
			for(int j = 0; j < m; ++j){
				scanf("%d",&bd[i][j]);
				row[0][i] = max(row[0][i],bd[i][j]);
				row[1][i] = min(row[1][i],bd[i][j]);
				col[0][j] = max(col[0][j],bd[i][j]);
				col[1][j] = min(col[1][j],bd[i][j]);
			}
		}
		bool flag = true;
		for(int i = 0; i < n && flag; ++i){
			for(int j = 0; j < m; ++j){
				if(bd[i][j] != row[0][i] && bd[i][j] != col[0][j]){
					flag = false;
					break;
				}
			}
		}
		flag?puts("YES"):puts("NO");
	}
	return 0;
}
