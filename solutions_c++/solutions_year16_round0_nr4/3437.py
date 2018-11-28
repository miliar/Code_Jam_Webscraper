#include<bits/stdc++.h>
using namespace std;
int main(){
	freopen("D-small-attempt0.in","r",stdin);
	freopen("out","w",stdout);
	int n,k,l,m;
	scanf("%d",&n);
	for(int i=1 ; i<=n ; i++){
		scanf("%d %d %d",&k,&l,&m);
		printf("Case #%d: ",i);
		for(int j=1 ; j<=m ; j++){
			printf("%d ",j);
		}
		printf("\n");
	}
	return 0;
}
