#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int t,i,ii,j,k,ok,sumx,sumo,sumt;
char s[10][10];

int main()
{
	scanf("%d\n",&t);
	for (ii=1; ii<=t; ii++)
	{
		for (i=0; i<=4; i++)
		    gets(s[i]);

		ok=0;
		for (i=0; i<=3; i++)
		{
			sumx=sumo=sumt=0;
		    for (j=0; j<=3; j++)
		        if (s[i][j]=='X')
		            sumx++;
				else
				if (s[i][j]=='O')
				    sumo++;
				else
				if (s[i][j]=='T')
				    sumt++;

			if (sumx+sumt==4)
			{
				ok=1;
				break;
			}
			else
			if (sumo+sumt==4)
			{
				ok=2;
				break;
			}
		}

		if (ok==0)
		{
            for (j=0; j<=3; j++)
			{
				sumx=sumo=sumt=0;
		    	for (i=0; i<=3; i++)
		        	if (s[i][j]=='X')
		            	sumx++;
					else
					if (s[i][j]=='O')
					    sumo++;
					else
					if (s[i][j]=='T')
					    sumt++;

				if (sumx+sumt==4)
				{
					ok=1;
					break;
				}
				else
				if (sumo+sumt==4)
				{
					ok=2;
					break;
				}
			}
		}

		if (ok==0)
		{
            sumx=sumo=sumt=0;
			for (i=0; i<=3; i++)
			    if (s[i][i]=='X')
			        sumx++;
				else
				if (s[i][i]=='O')
				    sumo++;
				else
				if (s[i][i]=='T')
				    sumt++;

			if (sumx+sumt==4)
			    ok=1;
			else
			if (sumo+sumt==4)
			    ok=2;
		}

		if (ok==0)
		{
            sumx=sumo=sumt=0;
			for (i=0; i<=3; i++)
			    if (s[i][3-i]=='X')
			        sumx++;
				else
				if (s[i][3-i]=='O')
				    sumo++;
				else
				if (s[i][3-i]=='T')
				    sumt++;

			if (sumx+sumt==4)
			    ok=1;
			else
			if (sumo+sumt==4)
			    ok=2;
		}

		if (ok==0)
		{
			for (i=0; i<=3; i++)
			    for (j=0; j<=3; j++)
			        if (s[i][j]=='.')
			            ok=4;
		}

		if (ok==0)
		    ok=3;

		printf("Case #%d: ",ii);
		if (ok==1)
		    printf("X won\n");
		else
		if (ok==2)
		    printf("O won\n");
		else
		if (ok==3)
		    printf("Draw\n");
		else
			printf("Game has not completed\n");
	}

	return 0;
}
