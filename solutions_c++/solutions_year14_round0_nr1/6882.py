#include<stdio.h>
#include<stdlib.h>

int main(){
FILE *pt=fopen("in2.txt","r");
FILE *po = fopen("out2.txt","w");

int t,i,j,n=0,ans1,ans2,ans;
int cards1[4][4],cards2[4][4],b1[18],found=0;
fscanf(pt,"%d",&t);

while(t--){
	n++;
	fscanf(pt,"%d",&ans1);
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			fscanf(pt,"%d",&cards1[i][j]);
		}
	}	

	fscanf(pt,"%d",&ans2);
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			fscanf(pt,"%d",&cards2[i][j]);
		}
	}	
	
	
	for(i=0;i<17;i++){
		b1[i]=0;
	}
	found=0;
	for(i=0;i<4;i++){
		b1[cards1[ans1-1][i]]=1;
	}	
	
	for(i=0;i<4;i++){
		if(b1[cards2[ans2-1][i]]==1){
			if(found==1){
				found = 2;
				break;
			}
			else{
				found = 1;
				ans=cards2[ans2-1][i];
			}
						
		}
	
	}
	
	if(found==0){
			fprintf(po,"Case #%d: Volunteer cheated!\n",n);
	}
	if(found==1){
			fprintf(po,"Case #%d: %d\n",n,ans);
	}
	if(found==2){
			fprintf(po,"Case #%d: Bad magician!\n",n);
	
	}
	
	
}
fclose(pt);
fclose(po);



}
