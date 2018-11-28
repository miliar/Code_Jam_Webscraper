#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){
	int t;
	int n,m;
	int i,j,k,l;
	FILE *fp_in,*fp_out;
	int **jan;
	int **arr;
	int *max,cur;
	int error;


	fp_in = fopen("B-large.in","r");
	fp_out = fopen("B-large.out","w");
	fscanf(fp_in,"%d\n",&t);
	
	for(i=0;i<t;i++){
		error = 0;
		fscanf(fp_in,"%d %d\n",&n,&m);
		max = (int*)malloc(sizeof(int)*n);
		jan = (int**)malloc(sizeof(int*)*n);
		arr = (int**)malloc(sizeof(int*)*n);
		for(j=0;j<n;j++){
			jan[j] = (int*)malloc(sizeof(int)*m);
			arr[j] = (int*)malloc(sizeof(int)*m);
			for(k=0;k<m;k++){
				fscanf(fp_in,"%d ",&jan[j][k]);
				arr[j][k] = 100;
			}
		}
		
		for(j=0;j<n;j++){
			max[j] = -1;
			for(k=0;k<m;k++){
				if(jan[j][k]>max[j]){
					max[j] = jan[j][k];
				}
			}

			for(k=0;k<m;k++){
				arr[j][k] = max[j];
			}
		}
		for(j=0;j<n&!error;j++){
			for(k=0;k<m&!error;k++){
				if(jan[j][k] < max[j]){
					cur = jan[j][k];
					for(l=0;l<n&!error;l++){
						if(jan[l][k] > cur){
							error = 1;
							break;
						}
					}
				}
			}
		}
		if(error == 0){
			fprintf(fp_out,"Case #%d: YES\n",i+1);
		}else
			fprintf(fp_out,"Case #%d: NO\n",i+1);
	}
}