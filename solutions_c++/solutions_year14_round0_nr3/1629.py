#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>

void main()
{
int cases, index_cases, M, R, C, i, j, possible, type,safe, even, dir;
int fullcols, lines, adj, rem, par;

freopen("C-large.in" , "rt" , stdin ) ;
freopen("C-large.out" , "wt" , stdout ) ;
//freopen("B-large.in" , "rt" , stdin ) ;
//freopen("B-large.out" , "wt" , stdout ) ;

cases = 0;
//read the number of test cases 
scanf("%d",&cases);
//printf("Cases = %d\n",cases);

//Loop through all the cases
for (index_cases=0 ; index_cases<cases; index_cases++)
{
	possible = 0;
	type=0;
	scanf("%d",&R);
	scanf("%d",&C);
	scanf("%d",&M);
	safe = R*C-M;
	even = M%2;
//printf("M=%d - %d ",M, even);	
	if (M==0)
	{
		type = 1;
		possible = 1;
	}
	else if((R==1)||(C==1))
	{
		type = 2;
		possible = 1;
	}
	else if (M==((R*C)-1))
	{
		type = 3;
		possible = 1;
	}
	else if (((R==2)||(C==2))&&(even==0)&&(safe > 2))
	{
		type = 4;
		possible = 1;
//		printf("safe %d, %d\n",safe, even);
	}
	else if ((R>2) && (C>2))
	{
		if (safe>7)
		{
			type = 5;
			possible = 1;
		}
		else if (safe==6)
		{
			type = 6;
			possible = 1;
		}
		else if (safe==4)
		{
			type = 7;
			possible = 1;
		}
	}

	printf("Case #%d:\n",index_cases+1);
	if (possible ==0) printf("Impossible\n");
	else if (type==1)
	{
		for(i=0; i< R; i++)
		{
			for (j=0; j<C; j++)
			{
				if ((j==0)&&(i==0))
					printf("c");
				else
 					printf(".");
			}
			printf("\n");
		}
	}
	else if (type==2)
	{
		for(i=0; i< R; i++)
		{
			for (j=0; j<C; j++)
			{
				if ((j==C-1) &&(i==R-1))
					printf("c");
				else
				{
					if (((C*i)+j)<M)
						printf("*");
					else
						printf(".");
				}
			}
			printf("\n");
		}
	}
	else if (type==3)
	{
		for(i=0; i< R; i++)
		{
			for (j=0; j<C; j++)
			{
				if ((i==0)&&(j==0))
					printf("c");
				else
					printf("*");
			}
			printf("\n");
		}
	}
	else if (type==4)
	{
		if (R==2)dir = 1;
		else dir = 0;
		for(i=0; i< R; i++)
		{
			for (j=0; j<C; j++)
			{
				if ((j==C-1)&&(i==R-1))
					printf("c");
				else
				{
					if (((dir==1)&&(j<(M/2)))||((dir==0)&&(i<(M/2))))
						printf("*");
					else
						printf(".");
				}
			}
			printf("\n");
		}

	}
	else if (type==5)
	{
//	  printf("Safe %d\n",safe);
	  if (safe<= (2*C))
	  {
		  lines = 2;
		  par = safe%2;
		  if (par>0)
		  {
			  fullcols = (safe-3)/2;
			  rem =1;
			  adj = 2;
		  }
		  else
		  {
			  fullcols = ((safe)/2)-1;
			  rem =0;
			  adj = 0;
		  }
//		  printf("fullcols %d, rem %d, adj %d\n", fullcols, rem, adj);
	  }
	  else
	  {
		lines = safe/C;
		rem = safe%C;
//		printf("lines %d- Rem %d\n",lines, rem);
		if (rem ==1)
		{
			fullcols = C -1;
			if(lines ==2) 
				adj = 2;
			else if (lines >2) 
				adj = 1;
		}
		else 
		{
			fullcols = C;
			adj = 0;
		}
	  }
	  for(i=0; i< R; i++)
	  {
		for (j=0; j<C; j++)
		{
			if ((i==0)&&(j==0))
				printf("c");
			else
			{
			if ((i<lines) && (j<fullcols))
				printf(".");
			else if ((i<lines-adj) && (j==fullcols))
				printf(".");
			else if ((i == lines)&& (j<adj+rem))
				printf(".");
			else printf("*");
			}
		}
		printf("\n");
	  }

	}
	else if (type==6)
	{
	  for(i=0; i< R; i++)
	  {
		for (j=0; j<C; j++)
		{
			if ((i==0)&&(j==0))
				printf("c");
			else
			{
				if ((i<2) && (j<3))
					printf(".");
				else printf("*");
			}
		}
		printf("\n");
	  }

	}
	else if (type==7)
	{
	  for(i=0; i< R; i++)
	  {
		for (j=0; j<C; j++)
		{

			if ((i==0)&&(j==0))
					printf("c");
			else
			{
				if ((i<2) && (j<2))
					printf(".");
				else printf("*");
			}
		}
		printf("\n");
	  }
	}

}
fclose(stdin) ;
fclose(stdout) ;
}