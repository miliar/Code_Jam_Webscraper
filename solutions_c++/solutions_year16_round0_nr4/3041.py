#include<stdio.h>
int main()
{
	int t,x;
	scanf("%d",&t);
	for(x=1;x<=t;x++)
	{
		int k,c,s,i;
		scanf("%d %d %d",&k,&c,&s);
		FILE *fptr;
        fptr=fopen("output.txt","a");
        fprintf(fptr,"Case #%d: ",x);
        for(i=1;i<=s;i++)
        {
        	fprintf(fptr,"%d ",i);
		}
		fprintf(fptr,"\n");
	}
	return 0;
}
