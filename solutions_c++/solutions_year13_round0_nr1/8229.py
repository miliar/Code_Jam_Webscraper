#include <iostream>
#include <stdio.h>


using namespace std;



char func(char *m);


int main()
{

	FILE *fp;
	FILE *out;
	int T;	
	int i;	
	int x, y;
	int c;

	char *m;


	fp = fopen("A-small-attempt0.in","rb");

	if(fp==NULL)
	{
		cout << "nok" << endl;
		exit(0);
	}

	fscanf(fp, "%d",&T);

	
	out  = fopen("output.txt","w");

	m = (char *)calloc(4*4, sizeof(char));

	for(i=1; i<=T; i++)
	{

		for(x=0; x<4; x++)
				 fscanf(fp, "%s", &m[x*4]);


		c = func(m);
	
		if(c=='X')fprintf(out, "Case #%d: %c won\n", i, c);
		else if(c=='O')fprintf(out, "Case #%d: %c won\n", i, c);
		else if(c=='.')fprintf(out, "Case #%d: Game has not completed\n", i);
		else {
			fprintf(out, "Case #%d: Draw\n", i);
		}

	}


	fclose(out);
	fclose(fp);





	return(0);
}


char func(char *m)
{
	int x;
	char c;

	
	for(x=0; x<4; x++)
	{
		if(m[4*x]== '.')continue;
		c = m[4*x];  

		if(m[4*x+1]=='.')continue;
		
		if(c=='T')c = m[4*x+1];		
		else {
			if(m[4*x+1]!= c && m[4*x+1]!='T')continue;
		}

		if(m[4*x+2]!=c && m[4*x+2] != 'T')continue;

		if(m[4*x+3]==c ||m[4*x+3]=='T')return(c);

	}


	for(x=0; x<4; x++)
	{
		if(m[x]== '.')continue;
		c = m[x];  

		if(m[4*1+x]=='.')continue;
		
		if(c=='T')c = m[4*1+x];		
		else {
			if(m[4*1+x]!= c && m[4*1+x]!='T')continue;
		}

		if(m[4*2+x]!=c && m[4*2+x] != 'T')continue;

		if(m[4*3+x]==c ||m[4*3+x]=='T')return(c);

	}

	while(1)
	{

		if(m[0]=='.')break;
		c=m[0];

		if(m[4*1+1]=='.')break;
		
		if(c=='T')c = m[4*1+1];		
		else {
			if(m[4*1+1]!= c && m[4*1+1]!='T')break;
		}

		if(m[4*2+2]!=c && m[4*2+2] != 'T')break;

		if(m[4*3+3]==c ||m[4*3+3]=='T')return(c);
	}

	while(1)
	{

		if(m[3]=='.')break;
		c=m[3];

		if(m[4*1+2]=='.')break;
		
		if(c=='T')c = m[4*1+2];		
		else {
			if(m[4*1+2]!= c && m[4*1+2]!='T')break;
		}

		if(m[4*2+1]!=c && m[4*2+1] != 'T')break;

		if(m[4*3]==c ||m[4*3]=='T')return(c);
	}


	for(x=0; x<16; x++)if(m[x]=='.')return '.';

	return('D');
}

