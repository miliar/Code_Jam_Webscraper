#include<stdio.h>
void main()
{
	FILE *i,*o;
	i = fopen("ques.txt", "r");
    o = fopen("ans.txt", "w");
	double c,f,pr=2.0,x;
    double t;
	int te;
	fscanf(i, "%d\n", &te);
	for(int i1=0;i1<te;i1++)
	{
		pr=2.0;
		t=0.0;
		fscanf(i, "%lf\n", &c);
		//printf("%.7lf\n",c);
		fscanf(i, "%lf\n", &f);
		//printf("%.7lf\n",f);
         fscanf(i, "%lf\n", &x);
		// printf("%.7lf\n",x);

	while((x/pr)>((c/pr)+(x/(pr+f))))
	{
		t=t+c/pr;
		pr=pr+f;

	}
	t=t+x/pr;
//	printf("%0.7lf\n",t);
    fprintf(o,"Case #%d: %0.7lf\n",i1+1,t);

	}
	fclose(i);
      fclose(o);

}