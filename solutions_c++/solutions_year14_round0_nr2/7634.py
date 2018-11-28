#include<stdio.h>
int main()
{
	double C,F,X,f,t1,t2,t3,s;
	int T,t;
	FILE *fp=fopen("B-large.out","w");
	FILE *fr=fopen("B-large.in","r");
	fscanf(fr,"%d",&T);
	for(t=1;t<=T;t++)
	{
		fscanf(fr,"%lf%lf%lf",&C,&F,&X);
		f=2; s=0;
		t1=C/f;
		t2=t1+X/(f+F);
		t3=X/f;
		while(t3>t2)
		{
			f+=F; s+=t1;
			t1=C/f;
			t2=t1+X/(f+F);
			t3=X/f;
		}
		s+=t3;
		fprintf(fp,"Case #%d: %.7lf\n",t,s);	
	}
	fclose(fp);
	fclose(fr);
	return 0;
}
