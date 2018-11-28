#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<fstream>
#define IN_FILE "input.txt"
#define OUT_FILE "output.txt"
int main()
{	
	ofstream out;
	ifstream in;
	out.open(OUT_FILE)
	in.open(IN_FILE)
	int a,i,j,k;
	in>>a;
	int mata[4][4],matb[4][4],x,y;
	for(i=0;i<a;i++)
	{
		int c=0,z=0;
		in>>x;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				in>>mata[j][k]:
			}
		}
		in>>y;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				in>>matb[j][k];
			}
		}
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				if(mata[x-1][j]==matb[y-1][k])
				{
					c++;
					z=mata[x-1][j];
				}
			}
		}
		if(c==1)
		{
			out<<"Case #%d: %d\n",i+1,z;
		}
		if(c>1)
		{
			out<<"Case #%d: Bad magician!\n",i+1;
		}
		if(c==0)
		{
			out<<"Case #%d: Volunteer cheated!\n",i+1;
		}
		
		
		
	}
	
	
	
	
	return 0;
}
