#include <string>
#include <vector>
#include <map>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <stack>
#include <set>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <time.h>
using namespace std;
int a[101][101];
int n,m;
int f[101][101];
int pan1(int x,int y){
	int i,j;
	for(i=1;i<=m;i++) if(a[x][i]>1) return(0);
	return(1);
}
int pan2(int x,int y){
	int i,j;
	for(i=1;i<=n;i++) if(a[i][y]>1) return(0);
	return(1);
}
void work(){
	int i,j;
	scanf("%d%d",&n,&m);
	for(i=1;i<=n;i++){
		for(j=1;j<=m;j++){
			scanf("%d",&a[i][j]);
		}
	}
	for(i=1;i<=n;i++){
		for(j=1;j<=m;j++){
			if(a[i][j]==1){
				if(!(pan1(i,j)||pan2(i,j))){
					printf("NO\n");
					return;
				}
			}
		}
	}
	printf("YES\n");
}
int main(){
    //freopen("B-small-attempt0.in","r",stdin);
    //freopen("b.out","w",stdout);
    int T,i;
    scanf("%d",&T);
    for(i=1;i<=T;i++){
		printf("Case #%d: ",i);
		work();
	}
}
