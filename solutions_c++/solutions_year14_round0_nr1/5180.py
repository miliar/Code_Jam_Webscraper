#include<bits/stdc++.h>
int main()
{
	int i,j,t,a[5][5],b[5][5],k=1,ans1,ans2,c,idx;
	scanf("%d",&t);
	while(t--){
		scanf("%d",&ans1);
		for(i=1;i<5;i++){
			for(j=1;j<5;j++){
				scanf("%d",&a[i][j]);
			}
		}
		scanf("%d",&ans2);
		for(i=1;i<5;i++){
			for(j=1;j<5;j++){
				scanf("%d",&b[i][j]);
			}
		}
	
	c=0;
	for(i=1;i<5;i++){
		for(j=1;j<5;j++){
			if(a[ans1][i]==b[ans2][j]){
				idx=i;
				c++;
			}
		}
	}
	if(c==1){
		printf("Case #%d: %d\n",k++,a[ans1][idx]);
	}
	else if(c==0){
		printf("Case #%d: Volunteer cheated!\n",k++);
	}
	else{
		printf("Case #%d: Bad magician!\n",k++);
	}
  }
	return 0;
}
