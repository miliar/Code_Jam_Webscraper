#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <string.h>
#include <string>
#include <math.h>
#include <time.h>
#include <vector>
#include <queue>
#define MXN 6
#define MXX 21
using namespace std;
int T,a,b,map[MXN][MXN],map2[MXN][MXN],total,record;
bool flag[MXX];
inline void Init() {
	scanf("%d",&a);
	for(int i=1;i<=4;i++) for(int j=1;j<=4;j++) scanf("%d",&map[i][j]);
	scanf("%d",&b);
	for(int i=1;i<=4;i++) for(int j=1;j<=4;j++) scanf("%d",&map2[i][j]);
}
inline void solve(){
	scanf("%d",&T);
	for(int ii=1;ii<=T;ii++) {
		Init();
		//printf("%d\n",ii);
		//for(int i=1;i<=4;i++) {for(int j=1;j<=4;j++) printf("%d ",map2[i][j]);printf("\n");}
		total=0;
		for(int i=1;i<=16;i++) flag[i]=0;
		for(int i=1;i<=4;i++) flag[map[a][i]]=1;
		for(int i=1;i<=4;i++) if(flag[map2[b][i]]) {
			total++;record=map2[b][i];
		}
		printf("Case #%d: ",ii);
		if(total==1) printf("%d\n",record);
		else if(total==0) printf("Volunteer cheated!\n");
		else printf("Bad magician!\n");
	}
}
int main(){
	freopen("gcj14A.in","r",stdin);freopen("gcj14A.out","w",stdout);
	solve();
    return 0;
}

