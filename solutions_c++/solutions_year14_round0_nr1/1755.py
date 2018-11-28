#include <iostream>
#include<cstdio>
using namespace std;
int main()
{
	int a[4][4],b[4][4],i,j,ct,k=1,elem = 0;
	int p,q;
	int t;
    FILE *fin=fopen("A-small-attempt1.in","r");
    FILE *fout=fopen("A-small-attempt1.out","w");
	fscanf(fin,"%d",&t);
	while(t--)
	{
		ct=0;
		fscanf(fin,"%d",&p);
		p-=1;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				fscanf(fin,"%d",&a[i][j]);
			}
		}
		fscanf(fin,"%d",&q);
		q-=1;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				fscanf(fin,"%d",&b[i][j]);
			}
		}
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(a[p][i]==b[q][j])
				{
					ct++;
					elem=a[p][i];
				}
			}
		}
		if(ct==0)
		{
			fprintf(fout,"Case #%d: %s\n",k,"Volunteer cheated!");
		}
		else if(ct==1)
		{
			fprintf(fout,"Case #%d: %d\n",k,elem);
		}
		else
		{
			fprintf(fout,"Case #%d: %s\n",k,"Bad magician!");
		}
		k++;
	}
	return 0;
}