#include<stdio.h>
void main()
{
	int t,r1,r2,a[4][4],b[4][4],c,v;
	FILE *i,*o;
	i=fopen("ques.txt","r");
	o=fopen("ans.txt","w");
	fscanf(i,"%d\n",&t);
	for(int i1=0;i1<t;i1++)
	{
		c=0;
		fscanf(i,"%d\n",&r1);
		for(int k=0;k<4;k++)
			for(int l=0;l<4;l++)
              fscanf(i,"%d\n",&a[k][l]);

		fscanf(i,"%d\n",&r2);
		for(int k=0;k<4;k++)
			for(int l=0;l<4;l++)
              fscanf(i,"%d\n",&b[k][l]);
		for(int k=0;k<4;k++)
		{
			for(int l=0;l<4;l++)
			{
				if(a[r1-1][k]==b[r2-1][l])
				{
                    c++;
					v=a[r1-1][k];
				}
			}
		}
		if(c==0)
			 fprintf(o, "Case #%d: Volunteer cheated!\n", i1+1);
		else if(c==1)
			 fprintf(o, "Case #%d: %d\n", i1+1,v);
		else
			 fprintf(o, "Case #%d: Bad magician!\n", i1+1);


	}
}