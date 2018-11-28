#include<stdio.h>
#include<conio.h>
void main()
{
	int t,field[105][105],m,n,same,poss;
	scanf("%i",&t);
	for(int test=1;test<=t;test++)
	{

		scanf("%i %i",&m,&n);
		for(int x=0;x<m;x++)
		{
			for(int y=0;y<n;y++)
			{
				scanf("%i",&field[x][y]);
				//printf("%i ",field[x][y]);
			}
			//printf("\n");
		}
		for(int tinggi=1;tinggi<=100;tinggi++)
		{
			for(x=0;x<m;x++)
			{
				same=1;
				for(int y=0;y<n;y++)
				{
					if(field[x][y]!=tinggi)
					{
						if(field[x][y]!=0)
						{
							same=0;
							break;
						}
					}
				}
				if(same==1)
				{
					for(y=0;y<n;y++)
					{
						field[x][y]=0;
					}
				}
			}

			for(int y=0;y<n;y++)
			{
				same=1;
				for(int x=0;x<m;x++)
				{
					if(field[x][y]!=tinggi)
					{
						if(field[x][y]!=0)
						{
							same=0;
							break;
						}
					}
				}
				if(same==1)
				{
					for(x=0;x<m;x++)
					{
						field[x][y]=0;
					}
				}
			}

		}//end tinggi
	     /*	for(x=0;x<m;x++)
		{
			for(int y=0;y<n;y++)
			{
				printf("%i ",field[x][y]);
			}
			printf("\n");
		} */

		poss=1;
		for(x=0;x<m && poss==1;x++)
		{
			for(int y=0;y<n;y++)
			{
				if(field[x][y]!=0)
				{
					poss=0;
					break;
				}
			}
		}
		if(poss==1)
		{
			printf("Case #%i: YES\n",test);
		}
		else
		{
			printf("Case #%i: NO\n",test);
		}

	}//end case
}