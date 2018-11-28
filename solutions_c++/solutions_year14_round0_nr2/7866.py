#include<cstdio>
using namespace std;
int main()
{
	int i,j,t,T,a,b,p[4],q[4],temp,ans;	
	double c,f,x,cr;
	FILE *fp=fopen("B-large.in","r");
	FILE *ofp=fopen("B-large.out","w");
	
	fscanf(fp,"%d",&T);
	for(t=0;t<T;t++)
	{
		fscanf(fp,"%lf%lf%lf",&c,&f,&x);
		cr=2;		
		double ttime=0,v1,v2;
		while(1)
		{
			v1=((c/cr)+(x/(cr+f)));
			v2=(x/cr);
			if(v1>v2)
			{
				ttime+=v2;break;
			}
			else
			{
				ttime+=(c/cr);
				cr+=f;
			}
		}
		if(t==0) fprintf(ofp,"Case #%d: %.7lf",(t+1),ttime);
		else fprintf(ofp,"\nCase #%d: %.7lf",(t+1),ttime);
	
	}
	
	
	fclose(fp);	
	fclose(ofp);
	return 0;
}