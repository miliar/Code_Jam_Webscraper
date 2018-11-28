#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include<string.h>
#include<fstream>
struct mag
{
    int a[4][4],b[4][4];
    int x,y;
};
int main()
{
	FILE *f,*fp;
	f=fopen("D:\A-small-attempt1.in","r");
	fp=fopen("D:\output.in","w");
	int n=1,T;
	fscanf(f,"%d",&T);
	while(T--)
	{
		struct mag e;
		int x,y,i,j,k,p,t,count=0;
		fscanf(f,"%d",&x);
		i=j=0;
		while(i<4)
		{
		   fscanf(f,"%d %d %d %d",&e.a[i][0],&e.a[i][1],&e.a[i][2],&e.a[i][3]);
		   i++;
	    }
		fscanf(f,"%d",&y);
		i=0;
		while(i<4)
		{
		    fscanf(f,"%d %d %d %d",&e.b[i][0],&e.b[i][1],&e.b[i][2],&e.b[i][3]);
			if(i==y-1)
			{
				for(k=0;k<4;k++)
				{
					for(j=0;j<4;j++)
					if(e.b[y-1][k]==e.a[x-1][j])
					{
						count++;
						p=e.b[y-1][k];
					}
				}
			}
			i++;
		}
		if(count==0)
		fprintf(fp,"Case #%d: Volunteer cheated!\n",n++);
		else if(count==1)
		fprintf(fp,"Case #%d: %d\n",n++,p);
		else
		fprintf(fp,"Case #%d: Bad magician!\n",n++);
	}
	fclose(f);
	fclose(fp);
	return 0;
}
