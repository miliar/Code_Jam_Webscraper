#include<stdio.h>

int mat1[4][4], mat2[4][4];
void printCard(int[4],int[4]);
void finalMethod(void);

int main(){
int testCases,i;
scanf("%d",&testCases);
for(i=1;i<=testCases;i++){
	printf("Case #%d: ",i);
	finalMethod();
						}
return 0;
           }
           
void finalMethod(void){
	int first,second,i,j;
	int temp1[4] , temp2[4];
	
	scanf("%d",&first);
	
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			scanf("%d",&mat1[i][j]);
						}
					}
					
	for(j=0;j<4;j++){
		temp1[j]=mat1[first-1][j];
					}
				
	scanf("%d",&second);
	
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){//printf("reached here i=%d j= %d",i,j);	
			scanf("%d",&mat2[i][j]);
						}
					}
					
	for(j=0;j<4;j++){
		temp2[j]=mat2[second-1][j];
					}
								
	printCard(temp1,temp2);
				}
				
void printCard(int temp1[4],int temp2[4]){
	int i,j,num,count=0;
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			if(temp1[i]==temp2[j]){
				num=temp1[i];
				count++;
									}
						}
					}
	if(count==0)printf("Volunteer cheated!\n");
	if(count==1)printf("%d\n",num);
	if(count>=2)printf("Bad magician!\n");
	
	return;
									}
