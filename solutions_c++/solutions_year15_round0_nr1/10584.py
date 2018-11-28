#include<stdio.h>
#include<malloc.h>
int main(){
	int count=0,i,testcases,level,max,sum;
	int *s;
	FILE* f1=fopen("A-small-attempt0.in","r");
	fscanf(f1,"%d",&testcases);
	if(testcases>=1&&testcases<=100){
		FILE* f2=fopen("output.txt","w");
		for(i=0;i<testcases;i++){
			fscanf(f1,"%d",&max);
			if(max>=0 && max<=6){
				sum=0;	
				count=0;
				s=(int *)malloc(sizeof(int)*(max+1));
				for(level=0;level<=max;level++){
					fscanf(f1,"%1d",&s[level]);
					if(s[level]==0) continue;
					if(sum>=level){
						sum+=s[level];
						continue;
					}	
					count+=level-sum;
					sum+=s[level]+count;
				}
				free(s);
			}
			fprintf(f2,"Case #%d: %d\n",i+1,count);
		}
		fclose(f2);
	}
	fclose(f1);
}



