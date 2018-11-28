#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main()
{
	FILE *f1,*f2;
	f1=fopen("B-large.in","r");
	f2=fopen("out.txt","w");
	double c,f,x,time,pr,fu,prate;
	int t,k;
	fscanf(f1,"%d",&t);
	for(k=0;k<t;k++)
	{
		prate=2.0;
		time=0.0;

		fscanf(f1,"%lf %lf %lf",&c,&f,&x);
		for(;;)
		{
			pr=time+x/prate;
			fu=time+c/prate+x/(prate+f);
			if(pr>fu){
				

				time=time+c/prate;
				prate=prate+f;
			}
			if(pr<=fu)
				break;
		}
		fprintf(f2,"Case #%d: %.7lf\n",k+1,pr);


	}
	fclose(f1);
	fclose(f2);

}