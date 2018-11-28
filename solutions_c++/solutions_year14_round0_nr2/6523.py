#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>


int main()
{
	//FILE *fi=fopen("sample.in","r"), *fo=fopen("sample.out","w");
	//FILE *fi=fopen("B-small-attempt1.in","r"), *fo=fopen("B-samll-attempt1.out","w");
	FILE *fi=fopen("B-large.in","r"), *fo=fopen("B-large.out","w");
	if(!fi||!fo){printf("Error opening files!\n");getchar();return -1;}
	int T=0,i=0,j=0,k=0,l=0;
	double C=0, F=0, X=0, val=0,c=0,r=0,p=0;
	fscanf(fi,"%d",&T);
	for(i=0;i<T;++i)
	{
              val=0;c=0,p=0,r=2;
              fscanf(fi,"%lf%lf%lf",&C,&F,&X);
//              printf("%f %f %f\n",C,F,X);
              while(1)
              {
                     if(X/r<(C/r+(X/(r+F)))){val+=X/r;break;}
                     val+=C/r;r+=F;
                    // if(4==i){printf("val: %f\tr: %f\n",val,r);getchar();}
              }
              fprintf(fo,"Case #%d: %.10lf\n",i+1,val);
              printf("Case #%d: %.10lf\t%lf\n",i+1,val,r);
    }
	fflush(fo);fclose(fi);fclose(fo);
	getchar();return 0;
}
