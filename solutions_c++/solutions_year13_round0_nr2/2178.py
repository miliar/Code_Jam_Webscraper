#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <map>

using namespace std;

int main()

{
	FILE *fi,*fo;
	
	int i,j,t,tt,n,m,imax[200],jmax[200];
	int l[200][200];
	
	fi=fopen("B.in","r");
	fo=fopen("B.out","w");
	
	fscanf(fi,"%d\n",&t);
	
	for (tt=0;tt<t;tt++)
	{	
		fscanf(fi,"%d%d",&n,&m);
		for (i=0;i<n;i++) imax[i]=-1;
		for (j=0;j<m;j++) jmax[j]=-1;
		for (i=0;i<n;i++) for (j=0;j<m;j++) 
		{
			fscanf(fi,"%d",&l[i][j]);
			if (imax[i]<l[i][j]) imax[i]=l[i][j];
			if (jmax[j]<l[i][j]) jmax[j]=l[i][j];
		}
		bool pos=true;
		for (i=0;i<n;i++) for (j=0;j<m;j++) if (l[i][j]!=imax[i] && l[i][j]!=jmax[j])
		{
			pos=false;
			break;
		}
		
		if (pos) fprintf(fo,"Case #%d: YES\n",tt+1);		
		else fprintf(fo,"Case #%d: NO\n",tt+1);		
	}
	
	fclose(fi);
	fclose(fo);

	return 0;
}
