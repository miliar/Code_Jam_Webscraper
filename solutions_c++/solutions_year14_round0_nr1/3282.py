#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm> 
using namespace std;
#define maxn 110
int mark[maxn];
int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int t,i,j,k,r1,r2,cas;
	scanf("%d",&t);
	for(cas = 1; cas<=t; cas++){
		memset(mark,0,sizeof(mark));
		scanf("%d",&r1); 
		r1--;
		for (i = 0;i<4;i++)
			for (j = 0;j<4;j++){
				scanf("%d",&k);
				if (i==r1) mark[k] = 1;
			}
		scanf("%d",&r2); 
		r2--;
		int ans = 0,cnt = 0;
		for (i = 0;i<4;i++)
			for (j = 0;j<4;j++){
				scanf("%d",&k); 
				if (i==r2){
					if (mark[k]){
						ans = k;
						cnt++;
					}
				}
			}
		printf("Case #%d: ", cas);
		if (cnt==0) printf("Volunteer cheated!\n");
		else if (cnt!=1)  printf("Bad magician!\n");
		else printf("%d\n",ans);
	}
	return 0;
}
