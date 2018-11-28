#include<cstdio>
using namespace std;
int main()
{
	int i,j,t,T,a,b,p[4],q[4],temp,ans;	
	FILE *fp=fopen("A-small-attempt0.in","r");
	FILE *ofp=fopen("A-small-attempt0.out","w");
	
	fscanf(fp,"%d",&T);
	for(t=0;t<T;t++)
	{
		fscanf(fp,"%d",&a);
		for(i=0;i<4;i++)
		{
			if((i+1)==a) fscanf(fp,"%d%d%d%d",&p[0],&p[1],&p[2],&p[3]);
			else fscanf(fp,"%d%d%d%d",&temp,&temp,&temp,&temp);
		}
		fscanf(fp,"%d",&b);
		for(i=0;i<4;i++)
		{
			if((i+1)==b) fscanf(fp,"%d%d%d%d",&q[0],&q[1],&q[2],&q[3]);
			else fscanf(fp,"%d%d%d%d",&temp,&temp,&temp,&temp);
		}
		temp=0;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(p[i]==q[j])
				{
					ans=p[i];
					temp++;
				}
			}
		}
		if(temp>1)
		{
			if(t==0) fprintf(ofp,"Case #%d: Bad magician!",(t+1));
			else fprintf(ofp,"\nCase #%d: Bad magician!",(t+1));
		}
		else if(temp==0)
		{
			if(t==0)fprintf(ofp,"Case #%d: Volunteer cheated!",(t+1));
			else fprintf(ofp,"\nCase #%d: Volunteer cheated!",(t+1));
		}
		else
		{
			if(t==0)fprintf(ofp,"Case #%d: %d",(t+1),ans);
			else fprintf(ofp,"\nCase #%d: %d",(t+1),ans);
		}
	}
	
	
	fclose(fp);	
	fclose(ofp);
	return 0;
}