#include<stdio.h>
//#include<conio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}
int main()
{
	FILE *fp,*fo;
	fp=fopen("B-small-attempt0 (1).in","r");
	fo=fopen("bsmalloutputfinal2.txt","w");
	int t,i,j,k,cnt,test,ch,a,b;
	fscanf(fp,"%d",&t);
	for(test=1;test<=t;test++)
	{
		cnt=0;
		fscanf(fp,"%d %d %d",&a,&b,&k);
		for(i=0;i<a;i++)
		{
			for(j=0;j<b;j++)
			{
				ch=i&j;
				if(ch<k)
				cnt++;
			}
		}
		fprintf(fo,"Case #%d: %d\n",test,cnt);
	}
	return 0;
}
