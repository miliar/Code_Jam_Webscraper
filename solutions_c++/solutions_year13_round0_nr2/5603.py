#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
int a[100][100],mm,i,j,t,n,m,mal[100],mah[100],max,end;
int main()
	{
		FILE *fin,*fout;
		fin = fopen("text.in","r");
		fout = fopen("text.out", "w");
		fscanf(fin,"%d",&mm);
		for (t=0;t<mm;t++)
		{
			fprintf(fout,"Case #%d: ",t+1);
			memset(mal,sizeof(mal),0);
			memset(mah,sizeof(mah),0);
			memset(a,sizeof(a),0);
			end = 0;
			fscanf(fin,"%d %d",&n,&m);
			for (i=0;i<n;i++)
				{
					max = 0;
					for (j=0;j<m;j++)
					{
						fscanf(fin,"%d",&a[i][j]);
						if (max<a[i][j]) max = a[i][j];
					}
					mah[i]=max;
				}
			for (i=0;i<m;i++)
				{
					max = 0;
					for (j=0;j<n;j++)
					{
						if (max<a[j][i]) max = a[j][i];
					}
					mal[i]=max;
				}
			for (i=0;i<n;i++)
				for (j=0;j<m;j++)
				{
					if ((mal[j] > a[i][j])&&(mah[i] > a[i][j])&&(end == 0))
					{
						fprintf(fout,"NO\n");
						end = 1;
						break;	
					}
				}
			if (end == 0) fprintf(fout,"YES\n");
		}	
	}
