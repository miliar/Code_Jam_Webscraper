#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;
int main(){
	//freopen("A-small-attempt1.in","r",stdin);
	//freopen("A-small-attempt1.out","w",stdout);
	int i,j,m,n,T,k,map[5][5],flag[20],v,ans,vcase=0;
	scanf("%d",&T);
	while(T--){
		v=0;
		memset(flag,0,sizeof(flag));
		scanf("%d",&k);
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				scanf("%d",&map[i][j]);
		for(j=1;j<=4;j++){
			flag[map[k][j]]++;
		}
		scanf("%d",&k);
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				scanf("%d",&map[i][j]);
		for(j=1;j<=4;j++){
			flag[map[k][j]]++;
			if(flag[map[k][j]]==2){
				v++;
				ans=map[k][j];
			}
		}
		printf("Case #%d: ",++vcase);
		if(v==0) printf("Volunteer cheated!\n");
		else if(v==1) printf("%d\n",ans);
		else printf("Bad magician!\n");
	}
	return 0;
}