#include "iostream"
#include<stdio.h>
#include<conio.h>
using namespace std;
#define read fscanf
#define write fprintf
int main()
{
   FILE *fp_rd=NULL,*fp_wr=NULL;
   fp_rd=fopen("C:\\Users\\Souvik\\Desktop\\Google\\B-small-attempt1.in","rb");
   fp_wr=fopen("C:\\Users\\Souvik\\Desktop\\Google\\B-small-output11.out","wb");
   int T,nol=0,i=1;
   double c_r1,x_r1,c_r2,x_r2,C,F,X,rate,sum,psum;
   if (!fp_rd) {
		printf("\n Error: Read file 1 ");
		return -1;
	}
	if (!fp_wr) {
		printf("\n Error: write file 1 ");
		return -1;
	}
	read(fp_rd,"%d\n",&T);
	nol++;
	while(nol<=T){
		psum=0.0000000;
		sum=0.00000000;
		rate=2.0;
		read(fp_rd,"%lf %lf %lf\n",&C,&F,&X);
		do{
			c_r1=C/rate;
			x_r1=X/rate;
			c_r2=C/(rate+F);
			x_r2=X/(rate+F);
			psum=c_r1+x_r2-x_r1;
			if(psum<0.00000001)
			{
				rate+=F;
				sum+=c_r1;
			}
			else{
				sum+=x_r1;
				break;
			}
		}while(1);
		write(fp_wr,"%s","Case #");
		write(fp_wr,"%d",(nol/1));
	    write(fp_wr,": %.7lf\n",sum);
		nol++;
	}
	cout<<nol;
	getchar();
	return 0;
}
