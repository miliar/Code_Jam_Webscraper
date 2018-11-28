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
	char str[2010];
	int lett[30];
	int dig[10];
	fgets(str, 10, fin);

	for (int ti=0; ti<t; ti++)
	{
		fgets(str, 2010, fin);
		for (int i=0; i<30; i++)
		{
			lett[i] = 0;
		}
		int n = strlen(str);
		for (int i=0; i<n; i++)
		{
			lett[str[i]-'A']++;
		}
		for (int i=0; i<10; i++)
		{
			dig[i] = 0;
		}
		int td = lett['Z'-'A'];
		dig[0] = td;
		lett['Z'-'A'] -= td;
		lett['E'-'A'] -= td;
		lett['R'-'A'] -= td;
		lett['O'-'A'] -= td;

		td = lett['U'-'A'];
		dig[4] = td;
		lett['F'-'A'] -= td;
		lett['O'-'A'] -= td;
		lett['U'-'A'] -= td;
		lett['R'-'A'] -= td;

		td = lett['W'-'A'];
		dig[2] = td;
		lett['T'-'A'] -= td;
		lett['W'-'A'] -= td;
		lett['O'-'A'] -= td;
		
		td = lett['O'-'A'];
		dig[1] = td;
		lett['O'-'A'] -= td;
		lett['N'-'A'] -= td;
		lett['E'-'A'] -= td;

		td = lett['F'-'A'];
		dig[5] = td;
		lett['F'-'A'] -= td;
		lett['I'-'A'] -= td;
		lett['V'-'A'] -= td;
		lett['E'-'A'] -= td;

		td = lett['V'-'A'];
		dig[7] = td;
		lett['S'-'A'] -= td;
		lett['E'-'A'] -= td;
		lett['V'-'A'] -= td;
		lett['E'-'A'] -= td;
		lett['N'-'A'] -= td;

		td = lett['X'-'A'];
		dig[6] = td;
		lett['S'-'A'] -= td;
		lett['I'-'A'] -= td;
		lett['X'-'A'] -= td;

		td = lett['G'-'A'];
		dig[8] = td;
		lett['E'-'A'] -= td;
		lett['I'-'A'] -= td;
		lett['G'-'A'] -= td;
		lett['H'-'A'] -= td;
		lett['T'-'A'] -= td;

		td = lett['I'-'A'];
		dig[9] = td;
		lett['N'-'A'] -= td;
		lett['I'-'A'] -= td;
		lett['N'-'A'] -= td;
		lett['E'-'A'] -= td;

		td = lett['T'-'A'];
		dig[3] = td;



		fprintf(fout,"Case #%d: ", ti+1);
		for (int i = 0; i<10; i++)
		{
			for (int j=0; j<dig[i]; j++)
			{
				fprintf(fout,"%d", i);
			}
		}
		fprintf(fout,"\n");

	}
	fclose(fin);
	fclose(fout);
	return 0;
}