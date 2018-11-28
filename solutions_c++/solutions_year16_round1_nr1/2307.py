#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <vector>
#include <string>


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
	char ini[1005];

	fgets(ini,100,fin);
	for (int ti=0; ti<t; ti++)
	{
		int n,l;
		fgets(ini,1001,fin);

		n = strlen(ini);

		l = n-1;
		int i=1;
		std::string s;
		s = ini[0];
		for (i=1; i<n; i++)
		{

			if (ini[i] < s[0])
			{
				s = s + ini[i];
			} else
			{
				s = ini[i] + s;
			}
		}

		fprintf(fout,"Case #%d: %s\n", ti+1, s.c_str());

	}
	fclose(fin);
	fclose(fout);
	return 0;
}