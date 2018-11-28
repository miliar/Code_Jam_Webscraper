#include "stdio.h"
#include "stdlib.h"

int main(){
	FILE *ptr,*optr;
	ptr=fopen("A-small-attempt2.in","r");
	optr=fopen("output.out","w");
	int arr1[4][4]={0};
	int arr2[4][4]={0};
	int ans1,ans2; 

	int test_run;
	fscanf(ptr,"%d",&test_run);
	for(int run=0; run<test_run; run++){


		fscanf(ptr,"%d",&ans1);
		for( int row =0 ;row <4 ;row++){
			for( int col =0 ;col <4 ;col++){
				fscanf(ptr,"%d",&arr1[row][col]);

			}
		}



		fscanf(ptr,"%d",&ans2);
		for( int row =0 ;row <4 ;row++){
			for( int col =0 ;col <4 ;col++){
				fscanf(ptr,"%d",&arr2[row][col]);

			}
		}
		int correct=0;
		int value=0;
		for( int col =0 ;col <4 ;col++){
			for( int col2 =0 ;col2 <4 ;col2++){
				if(arr1[ans1-1][col]==arr2[ans2-1][col2]){
					correct++;
					value=arr1[ans1-1][col];
				}
			}
		}
		fprintf(optr,"CASE #%d: ",run+1);
		if(correct==1){
			fprintf(optr,"%d \n",value);
		}
		if(correct>1){
			fprintf(optr,"Bad magician! \n");
		}
		if(correct==0){
			fprintf(optr,"Volunteer cheated! \n");
		}
		


	}
	fclose(ptr);
	fclose(optr);




	return 0;
}