#include <stdio.h>
#include <stdlib.h>

typedef unsigned short int _int;

_int x, t;
char colmax[100], rowmax[100], lawn[100][100];
char colOk[100], rowOk[100];
char n, m, val, error;

void gorow(char, char);

void gocol(char row, char col)
{
	char c;
	if(error || colOk[col])
		return;
	
	char max = lawn[row][col];
	
	if(colmax[col] > max)
	{
		error = 1;
		return;
	}
	
	for(c = 0; c < m; c++)
	{
		if(c == col)
			continue;
		if(lawn[row][c] < max)
			gorow(row, c);
	}
	colOk[col] = 1;
}

void gorow(char row, char col)
{
	char c;
	if(error || rowOk[row])
		return;
	
	char max = lawn[row][col];
	
	if(rowmax[row] > max)
	{
		error = 1;
		return;
	}
	
	for(c = 0; c < n; c++)
	{
		if(c == row)
			continue;
		if(lawn[c][col] < max)
			gocol(c, col);
	}
	rowOk[row] = 1;
}

int main()
{
	char y, z;
	
    freopen("A-small.in", "r", stdin);
    freopen("outf.txt", "w", stdout);

    if(stdin == 0 || stdout == 0)
    {
    	printf("No file\n");
        return -1;
    }

    scanf("%d%c", &t, &x);
    
    for(x = 0; x < t; x++)
    {
    	error = 0;
    	scanf("%d %d", &n, &m);
    	
		for(z = 0; z < m; z++)
		{
			colmax[z] = 0;
			colOk[z] = 0;
		}
		
    	for(y = 0; y < n; y++)
    	{
    		rowmax[y] = 0;
    		rowOk[y] = 0;
    		for(z = 0; z < m; z++)
    		{
    			scanf("%d", &val);
    			lawn[y][z] = val;
    			if(rowmax[y] < val)
    				rowmax[y] = val;
    			if(colmax[z] < val)
    				colmax[z] = val;
    		}
    	}
    	
    	for(y = 0; y < n; y++)
    	{
    		for(z = 0; z < m; z++)
    		{
    			if(lawn[y][z] < rowmax[y])
    				gocol(y, z);
    		}
    	}
    	
    	if(error)
		    printf("Case #%d: NO\n", x + 1);
	    else
		    printf("Case #%d: YES\n", x + 1);
    }
    return 0;
}
