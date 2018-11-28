#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <functional>
#define MAX 1000000
char arr[100][MAX+1];
int chk[100][MAX+1];

int main(void){
	FILE *fp_in,*fp_out;
	int T;
	int i,j;
	
	int n;

	int tmp;


	fp_in = fopen("A-small-attempt0.in","r");
	fp_out = fopen("A-small-attempt0.out","w");

	fscanf(fp_in,"%d",&T);

	for(i=0;i<T;i++){
		fscanf(fp_in,"%s %d\n",arr[i],&n);
		tmp = 0;
		int sum = 0;
		for(j=strlen(arr[i])-1;j>=0;j--){
			if(arr[i][j] == 'i'||arr[i][j] == 'a'||arr[i][j] == 'e'||arr[i][j] == 'o'||arr[i][j] == 'u'){
				tmp = 0;
				continue;
			}
			else{
				tmp ++;
				chk[i][j] = tmp;
			}
		}

		//start
		int end;
		for(j=0;j<strlen(arr[i]);j++){
			end = 0;
			if(chk[i][j] >= n){
				//sum += (strlen(arr)-(j+n-1))*(j+1);
				for(int k=j-1;k>=0;k--){
					if(chk[i][k] >= n){
						sum += (strlen(arr[i])-(j+n)+1)*(j-k);
						end =1;
						break;
					}
				}
				
			if(end == 0)
				sum += (strlen(arr[i])-(j+n-1))*(j+1);
			}
		}
		
		fprintf(fp_out, "Case #%d: %d\n",i+1 ,sum);
	
	}
	




	fclose(fp_in);
	fclose(fp_out);
}