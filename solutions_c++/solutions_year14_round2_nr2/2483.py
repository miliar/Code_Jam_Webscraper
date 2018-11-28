#include<stdio.h>
int main()
{
	int t,a,b,k,i,j,cnt,tt;
	FILE *ipf=fopen("ip.txt","r");
	FILE *opf=fopen("op.txt","w");
	fscanf(ipf,"%d",&t);
	for(tt=1;tt<=t;tt++)
	{
		cnt=0;
		fscanf(ipf,"%d %d %d",&a,&b,&k);
		for(i=0;i<a;i++)
		for(j=0;j<b;j++)
		if((i&j)<k)
		cnt++;
		fprintf(opf,"Case #%d: %d\n",tt,cnt);
	}
	return 0;
}
