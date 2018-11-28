// mycode.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "math.h"

int _tmain(int argc, _TCHAR* argv[])
{
	int T,i,A,B,C,count,t2,t3,t4,t5,t6,i1,i2,F,t1;
	double j,E;
	FILE *fi,*fo;
	fi = fopen("C-small-attempt0.in","r");
	fo = fopen("output.txt","w");
	fscanf(fi,"%d",&T);
	for(i=1;i<=T;i++)
	{
		fscanf(fi,"%d %d",&A,&B);
		//fscanf(fi,"%d",&B);
	    count=0;
		for(j=A;j<=B;j++)
		{
			E=sqrt(j);
			C=j;
			F=E;
			if((F*F)==C)
			{
				if(C<10)
				{
					t1=(C%10);
					i1=t1;
				}
				if(C>=10 && C<100)
				{
					t1=(C/10);
					t2=(C%10);
					i1=(t1+(t2*10));
				}
				if(C>=100 && C<1000)
				{
					t1=(C/100);
					t2=(C%100);
					t3=(t2/10);
					t4=(t2%10);
					i1=(t4+(10*t3)+(100*t1));
				}
				if(C==1000)
				{
					i1=1;
				}
				if(i1==C)
				{
					if(F<10)
					{
						t1=(F%10);
						i2=t1;
					}
					if(F>=10 && F<100)
					{
						t1=(F/10);
						t2=(F%10);
						i2=(t1+(t2*10));
					}
					if(F==i2)
					{
						count=count+1;
					}
				}
			}
		}
		fprintf(fo,"Case #%d: %d",i,count);
		fprintf(fo,"\n");
	}
	fclose(fo);
	fclose(fi);
	return 0;
}

