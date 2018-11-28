#include "iostream"
#include<stdio.h>
#include<conio.h>
using namespace std;
#define read fscanf
#define write fprintf
int main()
{
   FILE *fp_rd=NULL,*fp_wr=NULL;
   fp_rd=fopen("C:\\Users\\Souvik\\Desktop\\Google\\A-small-attempt0.in","rb");
   fp_wr=fopen("C:\\Users\\Souvik\\Desktop\\Google\\Download A-small-output0.in","wb");
   int arr1[4][4],arr2[4][4],T,r1,r2,nol=0,i,j,count,pos;
   if (!fp_rd) {
		printf("\n Error: Read file 1 ");
		return -1;
	}
	if (!fp_wr) {
		printf("\n Error: write file 1 ");
		return -1;
	}
	read(fp_rd,"%d\n",&T);
	printf("%d\n",T);
	while(nol<(10*T)){
		count=0;
		read(fp_rd,"%d\n",&r1);
		nol++;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++)
				read(fp_rd,"%d ",&arr1[i][j]);
			read(fp_rd,"\n");
			nol++;
		}
		read(fp_rd,"%d\n",&r2);
		nol++;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++)
				read(fp_rd,"%d ",&arr2[i][j]);
			read(fp_rd,"\n");
			nol++;
		}
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				if(arr1[r1-1][i]==arr2[r2-1][j])
				{	pos=i;
					count++;
				}
			}
		}
		if(count>1)
		{	
			write(fp_wr,"%s","Case #");
		    write(fp_wr,"%d",(nol/10));
			write(fp_wr,": %s\n","Bad Magician!");
		}
		if(count==1){
			write(fp_wr,"%s","Case #");
			write(fp_wr,"%d",(nol/10));
			write(fp_wr,": %d\n",arr1[r1-1][pos]);
		}
		if(count==0){
		    write(fp_wr,"%s","Case #");
		    write(fp_wr,"%d",(nol/10));
			write(fp_wr,": %s\n","Volunteer cheated!");
		}
		
	}
	fclose(fp_wr);
	fclose(fp_rd);
	return 0;
}