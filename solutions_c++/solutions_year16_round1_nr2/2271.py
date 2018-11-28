#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <vector>


int main(int argc, char *argv[])
{
	FILE *fin, *fout;
	if (argc > 1)
	{
		char tname[200];
		fin = fopen(argv[1],"r");
		strncpy (tname,argv[1],200);
		strncpy(strstr (tname,".in"),".out",4);
		fout = fopen(tname,"w");
	} else {
		fin = fopen("A.in","r");
		fout = fopen("A.out","w");
	}


	int t;
	fscanf(fin,"%d",&t);
	int inlist[5000];
	int mislist[50];
	for (int ti=0; ti<t; ti++)
	{
		int n,l;
		fscanf(fin,"%d", &n);
		l = n*(2*n-1);
		for (int i=0; i<l; i++)
		{
			fscanf(fin,"%d", inlist+i);
		}
		std::sort(inlist, inlist+l);
		int j = 0;
		for (int i=0; i<l-1; )
		{
			if (inlist[i] == inlist[i+1])
			{
				i+=2;
			} 
			else
			{
				mislist[j++] = inlist[i++];
			}
		}
		if (j<n)
		{
			mislist[n-1] = inlist[l-1];
		}

		fprintf(fout,"Case #%d:", ti+1);
		for (int i=0;i<n; i++)
		{
			fprintf(fout," %d", mislist[i]);
		}
		fprintf(fout," \n");
	}
	fclose(fin);
	fclose(fout);
	return 0;
}