#include <stdio.h>
#include <string.h>
#include <iostream.h>

#define LEN 70

typedef unsigned short int _int;

int main()
{
    char str[4][5], rows[4], cols[4], diagLT, diagRT, y, z, st, incom, dotindex;
    _int x, t;

    freopen("A-small.in", "r", stdin);
    freopen("outf.txt", "w", stdout);

    if(stdin == 0 || stdout == 0)
    {
    	printf("No file\n");
        return -1;
    }

    scanf("%hd%c", &t, &x);

	x = 0;
cases:
    for(; x < t; x++)
    {
    	incom = 0;
    	for(y = 0; y < 4; y++)
    		cols[y] = 1;
   		diagLT = diagRT = 1;
   		
		//read & check completeness
    	for(y = 0; y < 4; y++)
		{
	        scanf("%s", str[y]);
	        
	        //does column not have a dot?
			rows[y] = (dotindex = strchr(str[y], '.') - str[y]) < 0;
			while(dotindex >= 0)
			{
				incom = 1;
				
				cols[dotindex] = 0;
				if(y == dotindex)
					diagLT = 0;
				else if(y == 3 - dotindex)
					diagRT = 0;
				
				dotindex = strchr(str[y] + dotindex + 1, '.') - str[y];
				if(dotindex > 3)
					break;
			}
		}
		
		//check rows
		y = 0;
rowcheck:
    	for(; y < 4; y++)
		{
	        if(!rows[y])	//incomplete
	        	continue;

	        z = 1;
	        if((st = str[y][0]) == 'T')
	        {
	        	st = str[y][1];
	        	z = 2;
	        }
	        
			for(; z < 4; z++)
				if(str[y][z] != st && str[y][z] != 'T')
				{
					y++;
					goto rowcheck;
				}
			
			//st won
	        printf("Case #%d: %c won\n", x + 1, st);
	        x++;
	        goto cases;
    	}

		y = 0;
colcheck:	    
	    //check columns
		for(; y < 4; y++)
		{
			if(!cols[y])
				continue;
			
	        z = 1;
	        if((st = str[0][y]) == 'T')
	        {
	        	st = str[1][y];
	        	z = 2;
	        }
	        
			for(; z < 4; z++)
				if(str[z][y] != st && str[y][z] != 'T')
				{
					y++;
					goto colcheck;
				}
			
			//st won
	        printf("Case #%d: %c won\n", x + 1, st);
	        x++;
	        goto cases;
		}

		//diagonal LT-RB
		if(diagLT)
		{
	        z = 1;
	        if((st = str[0][0]) == 'T')
	        {
	        	st = str[1][1];
	        	z = 2;
	        }
	        
			for(; z < 4; z++)
				if(str[z][z] != st && str[z][z] != 'T')
					break;
			
			if(z == 4)
			{
		        printf("Case #%d: %c won\n", x + 1, st);
		        x++;
		        goto cases;
			}
		}
		
		//diagonal RT-LB
		if(diagRT)
		{
	        z = 1;
	        if((st = str[0][3]) == 'T')
	        {
	        	st = str[1][2];
	        	z = 2;
	        }
	        
			for(; z < 4; z++)
				if(str[z][3 - z] != st && str[z][3 - z] != 'T')
					break;
			
			if(z == 4)
			{
		        printf("Case #%d: %c won\n", x + 1, st);
		        x++;
		        goto cases;
			}
		}
		
		if(incom)
	        printf("Case #%d: Game has not completed\n", x + 1);
		else
	        printf("Case #%d: Draw\n", x + 1);
    }
    return 0;
}
