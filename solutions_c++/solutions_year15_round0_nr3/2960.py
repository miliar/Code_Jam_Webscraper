#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>

const int MAX=20000; 

char multc(int a, int b, int& m)
{
	if(a=='1' && b=='1') 
	{ return '1'; }
	else if(a=='1' && b=='i')
	{ return 'i'; }
	else if(a=='1' && b=='j')
	{ return 'j'; }
	else if(a=='1' && b=='k')
	{ return 'k'; }
	else if(a=='i' && b=='1')
	{ return 'i'; }
	else if(a=='i' && b=='i')
	{ m++; return '1'; }
	else if(a=='i' && b=='j')
	{ return 'k'; }
	else if(a=='i' && b=='k')
	{ m++; return 'j'; }
	else if(a=='j' && b=='1')
	{ return 'j'; }
	else if(a=='j' && b=='i')
	{ m++; return 'k'; }
	else if(a=='j' && b=='j')
	{ m++; return '1'; }
	else if(a=='j' && b=='k')
	{ return 'i'; }
	else if(a=='k' && b=='1')
	{ return 'k'; }
	else if(a=='k' && b=='i')
	{ return 'j'; }
	else if(a=='k' && b=='j')
	{ m++; return 'i'; }
	else if(a=='k' && b=='k')
	{ m++; return '1'; }
}

char divc(int a, int b, int& m)
{
	if(a=='1' && b=='1') 
	{ return '1'; }
	else if(a=='1' && b=='i')
	{ m++; return 'i'; }
	else if(a=='1' && b=='j')
	{ m++; return 'j'; }
	else if(a=='1' && b=='k')
	{ m++; return 'k'; }
	else if(a=='i' && b=='1')
	{ return 'i'; }
	else if(a=='i' && b=='i')
	{ return '1'; }
	else if(a=='i' && b=='j')
	{ return 'k'; }
	else if(a=='i' && b=='k')
	{ m++; return 'j'; }
	else if(a=='j' && b=='1')
	{ m++; return 'j'; }
	else if(a=='j' && b=='i')
	{ m++; return 'k'; }
	else if(a=='j' && b=='j')
	{ return '1'; }
	else if(a=='j' && b=='k')
	{ return 'i'; }
	else if(a=='k' && b=='1')
	{ return 'k'; }
	else if(a=='k' && b=='i')
	{ return 'j'; }
	else if(a=='k' && b=='j')
	{ m++; return 'i'; }
	else if(a=='k' && b=='k')
	{ return '1'; }
}

char mult(char* s, int l, int& m)
{
	char res='1';
	m=0;
	for(int i=0; i<l; i++) res=multc(res, *(s+i), m);
	return res;
}

int main()
{

	FILE* inf= fopen("input.txt", "r");
	FILE* outf= fopen("output.txt", "w");

	int T, L, X;
	fscanf(inf, "%d", &T);
	char s[MAX];
	char str[MAX];
	char ms[MAX];
	char mres[MAX];
	int min[MAX];
	memset(min, false, sizeof(min));
	strcpy(str, "");

	for(int i=1; i<=T; i++)
	{
		fscanf(inf, "%d %d", &L, &X);
		fscanf(inf, "%s", &s);

		strcpy(str, "");
		for(int j=1; j<=X; j++)
			strcat(str, s);

		int m;

		int lim=strlen(str);
		memset(min, false, sizeof(min));
		for(int j=1; j<=lim; j++)
		{
			m=0;
			mres[j-1]=mult(str, j, m);
			if(m%2==1) min[j-1]=1;
			else min[j-1]=0;
		}

		bool res=false;

		for(int s1=0; (s1<lim-1)&&(res==false); s1++)
			for(int s2=s1+1; (s2<lim)&&(res==false); s2++)
			{
				
				int minus=min[s1];
				if(mres[s1]!='i' || min[s1]!=0) continue;

				minus=min[s2];
				char cres=divc(mres[s2], mres[s1], minus);
				if(cres!='j' || minus%2!=0) continue;

				minus=min[lim-1];
				cres=divc(mres[lim-1], mres[s2], minus);
				if(cres!='k' || minus%2!=0) continue;

				res=true;
			}
			if(res) fprintf(outf, "Case #%d: YES\n", i);
			else fprintf(outf, "Case #%d: NO\n", i);
	}

	return 0;
}