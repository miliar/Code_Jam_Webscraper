using namespace std;
#include <iostream>
int main()
{
	int n,i,j,*p,m1,m2,a;

	FILE *fp1,*fp2;
	if((fp1=fopen("A-large.in","r"))==NULL)
	{
		printf("Cannot open this file\n");
		exit(0);
	}
	fp2=fopen("A-large.out","w");
	int t,h;
	fscanf(fp1,"%d\n",&t);
	for(h=0;h<t;h++)
	{
	m1=0,m2=0,a=0;
	fscanf(fp1,"%d\n",&n);
	p=new int[n];
	for(i=0;i<n;i++)
	{
		fscanf(fp1,"%d",&p[i]);
	}
	for(i=0;i<n-1;i++)
		if(p[i]>p[i+1])
		{
			m1+=p[i]-p[i+1];
			if(p[i]-p[i+1]>a)
				a=p[i]-p[i+1];
		}
	for(i=0;i<n-1;i++)
	{
		if(p[i]<a)
			m2+=p[i];
		else
			m2+=a;
	}
	fprintf(fp2,"Case #%d: %d %d\n",h+1,m1,m2);
	printf("Case #%d: %d %d\n",h+1,m1,m2);
	}
	fclose(fp1);
	fclose(fp2);

	getchar();
	getchar();
	return 0;
}