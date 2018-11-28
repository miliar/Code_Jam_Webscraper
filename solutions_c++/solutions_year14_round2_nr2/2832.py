#include<cstdio>
using namespace std;
int main()
{
	int i,j,t,T,a,b,k,ans;	
	FILE *fp=fopen("B-small-attempt0.in","r");
	FILE *ofp=fopen("B-small-attempt0.out","w");
	
	fscanf(fp,"%d",&T);
	for(t=0;t<T;t++)
	{
		fscanf(fp,"%d%d%d",&a,&b,&k);
		ans=0;
		for(i=0;(i<a);i++)
		{
			for(j=0;j<b;j++)
			{
				if((i&j)<k)
				{
					ans++;
				}
			}
		}
		
		if(t==0) fprintf(ofp,"Case #%d: %d",(t+1),ans);
			else fprintf(ofp,"\nCase #%d: %d",(t+1),ans);
		
	}
	
	fclose(fp);	
	fclose(ofp);
	return 0;
}