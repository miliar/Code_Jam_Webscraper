#include<stdio.h>
#include<cstdio>
#include<string.h>
int checkfor(int,int);
int main(){
	int test=0,count=1;

		FILE *fp1;
	fp1=fopen("A-small-attempt2.txt","r+");
	FILE *fp2;
	fp2=fopen("output1.txt","w+");
	char numstr[0];
	fscanf(fp1,"%d\n",&test);

	while(test--){
				  int a[4][4],b[4][4],i,j,m,n,found=0,value=0;
  	              fscanf(fp1,"%d\n",&m);
				  for(i=0;i<4;i++){
					 				 for(j=0;j<4;j++){
					 				 				  fscanf(fp1,"%d",&a[i][j]);
									  				 }
					 }
 				  fscanf(fp1,"%d\n",&n);
 				   for(i=0;i<4;i++){
					 				 for(j=0;j<4;j++){
					 				 				  fscanf(fp1,"%d",&b[i][j]);
									  				 }
					 }
			  	for(i=0;i<4;i++){
 								 for(j=0;j<4;j++){
					 				  			  if(a[m-1][i]==b[n-1][j]){
  					   				   			  			value=a[m-1][i];			   
															 found++;
					 				  }
					 }
	}
				  if(found==0)
				  			  fprintf(fp2,"Case #%d: Volunteer cheated!\n",count);
				  else if(found==1)

				  	   		  fprintf(fp2,"Case #%d: %d\n",count,value);
				  else if(found<5)

				  	   		 fprintf(fp2,"Case #%d: Bad magician!\n",count);
				  count++;				   			   			  
	}
	fclose(fp1);
	fclose(fp2);
	return 0;
}

