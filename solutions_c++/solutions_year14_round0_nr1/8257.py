#include <stdio.h>
#include <algorithm>
int t;
int a[10][10];
int v[20];
int v2[20];
int cnt;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	int k;
	int r1,r2;
	for(k=1;k<=t;k++){
		std::fill(v,v+18,0);
		scanf("%d",&r1);
		int i,j;
		for(i=1;i<=4;i++){
			for(j=1;j<=4;j++){
				scanf("%d",&a[i][j]);
				if(i==r1) v[a[i][j]]=1;
			}
		}
		cnt=0;
		scanf("%d",&r2);
		for(i=1;i<=4;i++){
			for(j=1;j<=4;j++){
				scanf("%d",&a[i][j]);
				if(i==r2 && v[a[i][j]]==1) v2[++cnt]=a[i][j];
			}
		}
		printf("Case #%d: ",k);
		if(cnt==0) printf("Volunteer cheated!\n");
		else if(cnt==1) printf("%d\n",v2[1]);
		else printf("Bad magician!\n");
	}
	return 0;
}