#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;
int main()  
{
	FILE *fin,*fout;
	fin=fopen("B-large.in","rb");
	fout=fopen("B-large.out","wb");
	int r,t;
	double c,f,x,ct,now;
	fscanf(fin,"%d",&t);
	for(r=1;r<=t;r++)
	{
		fscanf(fin,"%lf%lf%lf",&c,&f,&x);
		ct=0;now=2;
		while(c/now+x/(now+f)<x/now)
		{
			ct+=c/now;
			now+=f;
		}
		ct+=x/now;
		fprintf(fout,"Case #%d: %.7f\n",r,ct);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}