#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int hash[17];
int data[5][5];
int main(){
	int i,j,k,t,ans1,ans2,cnt,result;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	scanf("%d",&t);
	for(i=1;i<=t;++i){
		memset(hash,0,sizeof(hash));
		scanf("%d",&ans1);
		for(j=1;j<=4;++j)
		for(k=1;k<=4;++k)
		scanf("%d",data[j]+k);
		for(j=1;j<=4;++j)
		hash[data[ans1][j]]=1;
		scanf("%d",&ans2);
		for(j=1;j<=4;++j)
		for(k=1;k<=4;++k)
		scanf("%d",data[j]+k);
		for(j=1,cnt=0;j<=4;++j){
			if(hash[data[ans2][j]])
			++cnt,result=data[ans2][j];
		}
		if(!cnt)
		printf("Case #%d: Volunteer cheated!\n",i);
		else if(cnt==1)
		printf("Case #%d: %d\n",i,result);
		else
		printf("Case #%d: Bad magician!\n",i);
	}
	return 0;
}
