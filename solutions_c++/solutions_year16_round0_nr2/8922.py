#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include<string.h>

int main(void){

	FILE *f1,*f2;
	f1=fopen("B-large.in","r+");
	f2=fopen("output_b_l.txt","w+");

	int t,cnt;
	int i,j,k,len;
	char cake[105];
	char temp;

	fscanf(f1,"%d",&t);
	cnt=1;
	while(t--){
		fscanf(f1,"%s",cake);
		fprintf(f2,"CASE #%d: ",cnt++);
		printf("%d\n",t);
		for(i=0;;i++){
			len=strlen(cake);
			//printf("%d  ",len);
			for(j=1;j<len;j++){
				if(cake[0]!=cake[j]){
					//printf("j=%d\n",j);
					for(k=0;k<j/2;k++){
						//printf("k=%d\n",k);
						temp=cake[k];
						cake[k]=cake[j-k-1];
						cake[j-k-1]=temp;
					}
					for(k=0;k<j;k++){
						if(cake[k]=='+'){
							cake[k]='-';
						}
						else if(cake[k]=='-'){
							cake[k]='+';
						}
					}
					//printf("%s\n",cake);
					break;
				}
			}		
			if(j==len){
				if(cake[0]=='-'){
					fprintf(f2,"%d\n",i+1);
				}
				else{
					fprintf(f2,"%d\n",i);
				}			
				break;
			}
		}
	}
	return 0;
}