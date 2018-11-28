#include <stdio.h>

#define MAX_GRID_SIZE	100
#define MAX_HEIGHT		100

FILE *fin, *fout;
int Lawn[MAX_GRID_SIZE][MAX_GRID_SIZE];
int lins[MAX_GRID_SIZE],cols[MAX_GRID_SIZE];	// no. of grids in each row/col that can be cut to the present height
int n,m;
bool heights[MAX_HEIGHT+1];		// keeps track of the desired lawn heights

int next_height (int h)		// returns the next desired height, strictly smaller than h
{
	int i;
	for (i = h-1; i >= 0; i--)
		if (heights[i])
			return i;
	return -1;
}


void solve ()
{
	int itest,ntests;
	int i,j,h,max_h;
	bool feasible;
	const char *res;

	fscanf (fin,"%d",&ntests);
	for (itest = 1; itest <= ntests; itest++)
	{
		// housekeeping
		for (i = 0; i <= MAX_HEIGHT; i++)
			heights[i] = false;
		max_h = 0;
		feasible = true;
	
		// read
		fscanf (fin,"%d%d",&n,&m);
		for (i = 0; i < n; i++)
			for (j = 0; j < m; j++)
			{
				fscanf (fin,"%d",&h);
				Lawn[i][j] = h;
				heights[h] = true;
				if (max_h < h)
					max_h = h;
			}
		
		// solve
		h = max_h;
		do
		{
			// determine which lines and cols can be fully cut to this height
			//first some housekeeping
			for (i = 0; i < n; i++)
				lins[i] = 0;
			for (j = 0; j < m; j++)
				cols[j] = 0;			
			//sweep the lawn to compute lins,cols
			for (i=0; i<n; i++)
				for (j=0; j<m; j++)
					if (Lawn[i][j] <= h)
					{
						lins[i]++;
						cols[j]++;
					}
			//sweep the lawn to see if all grids == h can be reached
			for (i=0; i<n && feasible; i++)
				for (j=0; j<m && feasible; j++)
					if (Lawn[i][j] == h)
						if (lins[i] != m && cols[j] != n)	// can't be reached
							feasible = false;
		
			h = next_height(h);
		}
		while (feasible && h > 0);
		// determine outcome
		if (feasible)
			res = "YES";
		else
			res = "NO";
		
		// report
		fprintf (fout,"Case #%d: %s\n",itest,res);
	}
}

int main (int argc, char **args)
{
	if (argc != 3)
	{
		printf ("Usage:\n\t%s <file_in> <file_out>\n",args[0]);
		return 1;
	}
	
	fin = fopen (args[1],"r");
	fout = fopen (args[2],"w");
	
	if (fin == NULL || fout == NULL)
	{
		printf ("Something's wrong with the in/out files!\n");
		return 1;
	}
	
	solve();
	
	fclose(fin);
	fclose(fout);
	return 0;
}

