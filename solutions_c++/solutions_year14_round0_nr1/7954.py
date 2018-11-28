#include<stdio.h>

int main(){

	int t;
	scanf("%d\n",&t);
	while(t!=0){
	
    int	arr1[4][4],arr2[4][4],i,j,r1,r2;
    scanf("%d\n",&r1);
	for(i=0;i<4;i++)
	for(j=0;j<4;j++){
	scanf("%d",&arr1[i][j]);
		
	}		
	scanf("%d\n",&r2);	
	for(i=0;i<4;i++)
	for(j=0;j<4;j++){
	scanf("%d",&arr2[i][j]);
		
	}	
	int count=0;		
	for(i=0;i<4;i++)
	for(j=0;j<4;j++){
	if(arr1[(r1-1)][i]==arr2[(r2-1)][j]){
		count++;
	}	
		
		
	}
	int p;
	if(count==1){
	for(i=0;i<4;i++)
	for(j=0;j<4;j++){
	if(arr1[(r1-1)][i]==arr2[(r2-1)][j]){
		p=i;
		break;	
		
}
		
	}
	printf("case #%d: %d\n",t,arr1[(r1-1)][p]);
}
	else if(count==0)
	printf("case #%d: Volunteer cheated!\n",t);
	else
	printf("case #%d: Bad magician!\n",t);		
		t--;
	}

	return 0;
}

