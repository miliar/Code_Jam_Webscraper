#include <stdio.h>
#include <limits.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;

int main(){
	freopen("E:\\C\\A-small-attempt0.in","r",stdin);
	freopen("E:\\C\\ans.txt","w",stdout);
	int t,cc=1;
	int arr[5][5];
	int mark[5];
	int ans,answer,tmp;
	int i,j;
	scanf("%d",&t);
	for(;cc<=t;cc++){
		answer=tmp=0;
		scanf("%d",&ans);
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				scanf("%d",&arr[i][j]);
		for(i=1;i<=4;i++)
			mark[i]=arr[ans][i];
		scanf("%d",&ans);
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				scanf("%d",&arr[i][j]);
		for(i=1;i<=4;i++){
			for(j=1;j<=4;j++){
				if(mark[i]==arr[ans][j]){
					answer++;
					tmp=mark[i];
				}
			}		
		}
		if(answer==1)
			printf("Case #%d: %d\n",cc,tmp);
		else if(answer>1)
			printf("Case #%d: Bad magician!\n",cc);
		else if(answer==0)
			printf("Case #%d: Volunteer cheated!\n",cc);
	}

	return 0;
}