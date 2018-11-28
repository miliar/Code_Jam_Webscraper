#include<stdio.h>
FILE *in,*out;
int b[17];
int main()
{
	in=fopen("a.in","r");
	out=fopen("a.out","w");
	int tc,test;
	int r,i,o;
	int a,s;
	fscanf(in,"%d",&tc);
	for(test=1;test<=tc;test++)
	{
		for(a=1;a<=16;a++) b[a]=0;
		fscanf(in,"%d",&r);
		for(a=1;a<=4;a++)
		{
			for(s=0;s<4;s++)
			{
				fscanf(in,"%d",&i);
				if( a==r ) b[i]=1;
			}
		}
		fscanf(in,"%d",&r);
		o=0;
		for(a=1;a<=4;a++)
		{
			for(s=0;s<4;s++)
			{
				fscanf(in,"%d",&i);
				if( a==r )
				{
					if( b[i]==1 )
					{
						if( o==0 ) o=i;
						else o=-1;
					}
				}
			}
		}
		fprintf(out,"Case #%d: ",test);
		if( o==-1 ) fprintf(out,"Bad magician!");
		else if( o==0 ) fprintf(out,"Volunteer cheated!");
		else fprintf(out,"%d",o);
		fprintf(out,"\n");
	}
	return 0;
}