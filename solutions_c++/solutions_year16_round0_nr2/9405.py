#include<cstdlib>
#include<iostream>
#include<fstream>
#include<cmath>
#include<cstdio>
#include<string.h>

using namespace std;


int main()
{
	char s[101];
	int t, lun, piu, meno, risultato;
	
	FILE *in = fopen("B-large.in", "r");
	FILE *out = fopen("output.txt", "w");
	fscanf(in,"%d",&t);
	
	for(int i=0; i<t; i++)
	{
		fscanf(in,"%s",s);
        //cout<<s[1]<<endl;
        lun=strlen(s);
        piu=0;
        meno=0;
        risultato=0;
        for(int j=0; j<lun; j++)
        {
			if((s[j]=='+')&&(piu==0))
        	{
        		piu=1;
				meno=0;
        		risultato++;
			}
			else if((s[j]=='-')&&(meno==0))
			{
				piu=0;
				meno=1;
				risultato++;
			}
		}
		if(s[lun-1]=='+')
			risultato--;
		fprintf(out,"Case #%d: %d\n",i+1,risultato);
	}
	fclose(in);
	fclose(out);
	system("PAUSE");
	return 0;
}

