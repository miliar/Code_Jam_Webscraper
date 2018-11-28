#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
	int cut[10][10];
} cut_t;

#define min(x, y) ((x<y) ? x : y)
#define max(x, y) ((x>y) ? x : y)

char* getNext(char** src, int sp)
{
        char* s = strchr(*src, sp);
        char* sorg = *src;

        if (NULL == s)
        {
                int n = strlen(*src);
                if (n > 1 && ((0x0a == sorg[n-1]) || (0x0d == sorg[n-1])))
                {
                        sorg[n-1] = 0;
                }
                if (n > 2 && ((0x0a == sorg[n-2]) || (0x0d == sorg[n-2])))
                {
                        sorg[n-2] = 0;
                }
                return sorg;
        }

        *s = 0;
        *src = s+1;
        return sorg;
}

int getNextNum(char** src, int sp)
{
        char* s = getNext(src, sp);
        if (NULL == s)
        {
                return 0;
        }
        else
        {
                return atoi(s);
        }
}

bool judgeCut(cut_t * g,unsigned int r,unsigned int c)
{	
	if (10 < r || 10 < c)
	{
		return false;
	}
	for (int i = 0; i < r; i++)
	{
		for (int j = 0; j < c; j++)
		{
			int maxNorth = g->cut[i][j];
			int maxSouth= g->cut[i][j];
			int maxWest = g->cut[i][j];
			int maxEast = g->cut[i][j];
			
			for (int k = 0; k < i; k++)
			{
				if (g->cut[k][j] > maxNorth)
				{
					maxNorth = g->cut[k][j];
				}
			}
			
			for (int k = i+1; k < r; k++)
                        {
                                if (g->cut[k][j] > maxSouth)
                                {
                                        maxSouth = g->cut[k][j];
                                }       
                        }

                        for (int k = 0; k < j; k++)
                        {
                                if (g->cut[i][k] > maxWest)
                                {
                                        maxWest = g->cut[i][k];
                                }
                        }

                        for (int k = j+1; k < c; k++)
                        {
                                if (g->cut[i][k] > maxEast)
                                {
                                        maxEast = g->cut[i][k];
                                }
                        }

			if ((g->cut[i][j]) < max(maxNorth, maxSouth) 
				&& (g->cut[i][j]) < max(maxEast, maxWest))
			{
				return false;
			}
			//printf(" %d", g->cut[i][j]);
		}
		//printf("\n");
	}

	return true;
}

int main (void)
{
	char line[2049] = {0};
	cut_t g;
	int resultx[10] = {0};
	int resulty[10] = {0};
	bool notComplete = false;
	char *p = NULL;
	FILE* f = NULL;
	int t = 0;
	int outline = 1;
	int n=0;
	int m=0;

	memset(&g, 0, sizeof(g));

	f = fopen("input.txt", "r");

	p = fgets(line, 2048, f);
	//get linenum
	sscanf(line, "%d", &t);

	for (int i = 0; i < t; i++)
	{
	        p = fgets(line, 2048, f);
      	        if (NULL == p)
               	{
                       	break;
               	}
	
		sscanf(line, "%d %d", &n, &m);
		//printf("n=%d, m=%d\n", n, m);

		for (int row = 0; row < 10 && row < n; row++)
		{
	        	p = fgets(line, 2048, f);
	      	        if (NULL == p)
                	{
                        	break;
                	}
	
			char* str = line;

			for (int colum = 0; colum < 10 && colum < m; colum++)
			{
				g.cut[row][colum] = getNextNum(&str, ' ');
				//printf(" %d", cut[row][colum]);
			}

			//printf("\n");
		}

		if (judgeCut(&g, (unsigned int) n, (unsigned int) m))
		{
			printf("Case #%d: YES\n", outline++);
		}
		else
		{
			printf("Case #%d: NO\n", outline++);
		}
	}
	
	fclose(f);
	return 0;
}
