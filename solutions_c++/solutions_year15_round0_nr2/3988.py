#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int comp(const void*a,const void*b)
{
return *(int*)b-*(int*)a;
}
void main(){
	int T,D,P[6];
	FILE *fp,*fp1;
	int i,j,time;

	fp=fopen("B-small-attempt4.in","r");
	fp1=fopen("out.txt","w");
	fscanf(fp,"%d\n",&T);
	for(i=0;i<T;i++){
		fscanf(fp,"%d\n",&D);
		for(j=0;j<D;j++)
			fscanf(fp,"%d",&P[j]);
		qsort(P,D,sizeof(int),comp);
		if(P[0]==1)
			time=1;
		else{
			if(D==1)
				time=(P[0]+1)/2+1;
			else{
				if(P[0]==P[1])
					time=P[0];
				else{
					if(((P[0]+1)/2)>=P[1])
						time=(P[0]+1)/2+1;
					else
						time=P[1]+1;
				}
			}
		}
		fprintf(fp1,"Case #%d: %d\n",i+1,time);
	}
	fclose(fp1);
	fclose(fp);
}