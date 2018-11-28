#include <iostream>
using namespace std;

int main() 
{
	int t,i,ansa,ansb,a[4][4],b[4][4],ctr,ans,j,k;
	FILE *ifp, *ofp;
	char outputFilename[] = "MagicTrickOutput.txt";
	
	ifp = fopen("A-small-attempt1.in", "r");
	ofp = fopen(outputFilename, "w");
	fscanf(ifp,"%d", &t);
	for(i=1;i<=t;i++)
	{
		fscanf(ifp,"%d",&ansa);
		ctr=0;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				fscanf(ifp,"%d",&a[j][k]);
			}
		}
		fscanf(ifp,"%d",&ansb);
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				fscanf(ifp,"%d",&b[j][k]);
			}
		}
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				if(a[ansa-1][j]==b[ansb-1][k])
				{
				     ctr++;
				     ans=a[ansa-1][j];
				}
			}
		}
		if(ctr==1)
			fprintf(ofp,"Case #%d: %d",i, ans);
		else if(ctr==0)
			fprintf(ofp,"Case #%d: Volunteer cheated!",i);
		else
			fprintf(ofp,"Case #%d: Bad magician!",i);
		
		if(i!=t)
		   fprintf(ofp,"\n");
	}
	return 0;
}
