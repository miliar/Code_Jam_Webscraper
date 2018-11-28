#include <stdio.h>
#define row 4
#define col 4
int main(){
	FILE *f;
	f=fopen("answer.txt","w");
	int a[row][col],b[row][col],see[4];
	int arow,brow,num,flag,answer;
	int z,i,j,k=1;
	scanf("%d",&z);
	while(k<=z){
		arow=brow=num=flag=answer=0;
		scanf("%d",&arow);
		for(j=0;j<row;j++){
			for(i=0;i<col;i++){
				scanf("%d",&a[j][i]);
			}
		}
		for(i=0;i<col;i++)
		see[i]=a[arow-1][i];
		scanf("%d",&brow);
		for(j=0;j<row;j++){
			for(i=0;i<col;i++){
				scanf("%d",&b[j][i]);
			}
		}
		for(j=0;j<4;j++){
			for(i=0;i<col;i++){
				if(b[brow-1][i]==see[j]){
					num++;
					if(flag==0){
						answer=see[j];
						flag++;
					}
				}
			}
		}
		fprintf(f,"Case #%d: ",k++);
		if(num==1)
			fprintf(f,"%d\n",answer);
		else if(num==0)
			fprintf(f,"Volunteer cheated!\n");
		else
			fprintf(f,"Bad magician!\n");
	}
	fclose(f);
}