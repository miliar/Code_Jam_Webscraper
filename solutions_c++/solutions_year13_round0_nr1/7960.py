#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <string.h>

char line[8][4];

char check(char line[4])
{
	long sum = 0;
	char ret = 'D';
	
	for(int i=0; i<4; i++)
	{
	    sum += line[i];
		
		if(line[i] == '.')
		   ret = 'N';
	}

	if((sum > (3*'X')) && ((sum % 'X') == 0) || ((sum % 'X') == 'T'))
		return 'X';

	if((sum >= (4*'O')) && ((sum % 'O') == 0) || ((sum % 'O') == ('T' - 'O')))
		return 'O';
		
	return ret;
}

int main()
{
	long long n = 0, ncases = 0;
	char res = 'D';

   	FILE *fin, *fout;

	fin = fopen("in1.txt", "r");
	if(!fin)
		return 1;
	
	fout = fopen("out1.txt", "w");
	if(!fout)
		return 1;    
	
	fscanf(fin, "%d\n", &ncases);

	for(n=0; n<ncases; n++)
	{
	    char i,j;
		char sout[50]; 
		for (i = 0; i<4; i++)
		{
			fscanf(fin, "%s\n", line[i]);
	    }

		for (i = 0; i<4; i++)
		{
			for(j=0; j<4; j++)
			{
			   line[4+i][j] =line[j][i];
			}	
            line[8][i] = line[i][i];
            line[9][i] = line[i][3-i];			
	    }
        
        for(i=0; i<10; i++)
		{
		   res = check(line[i]);
		   if((res == 'X') || (res == 'O')) 
		       break;		   
		}  
        switch (res)
        {
		   case 'X':
		      fprintf(fout, "Case #%d: X won\n", n+1, sout);
			  break;
		   case 'O':
		      fprintf(fout, "Case #%d: O won\n", n+1, sout);
			  break;
		   case 'D':
		      fprintf(fout, "Case #%d: Draw\n", n+1, sout);
			  break;
           default:
 		   	  fprintf(fout, "Case #%d: Game has not completed\n", n+1, sout);
			  break;
        }		
	}
	
	fclose(fin); fclose(fout);
}