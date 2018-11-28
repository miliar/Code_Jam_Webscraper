#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NUM 10000000

static unsigned long long fairtbl[1000];
static int fairtbllen;

#if 0
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

#endif

bool isFair(unsigned long long num)
{
	char fairstr[100] = {0};
	int len = 0;
        int d = 0;

        while (1)
        {
            d = num % 10;
            fairstr[len++] = d + '0';
            if (num < 0x0al)
            {
            	break;
            }
            num = (num - d) / 10;
        }

	for (int i= 0; i < len/2; i++)
	{
		if (fairstr[i] != fairstr[len - i -1])
		{
			return false;
		}
	}

	//printf("fairstr=%s\n", fairstr);

	return true;
}

void fairsquare()
{
	int len = 0;
	int d = 0;
	int index = 0;
	
	fairtbllen = 0;
	memset(&fairtbl, 0, sizeof(fairtbl));

	for (unsigned long i = 1; i < MAX_NUM; i++)
	{
		if (!isFair((unsigned long long) i))
		{
			continue;
		}

		unsigned long long sq = i * i;
		
		if (!isFair(sq))
		{
			continue;
		}

		//printf("%u^2 = %llu \n", i, sq);
		fairtbl[fairtbllen++] = sq;
	}
}

int main (void)
{
	char line[2049] = {0};
	bool notComplete = false;
	char *p = NULL;
	FILE* f = NULL;
	int t = 0;
	int outline = 1;
	unsigned long long a=0;
	unsigned long long b=0;

	fairsquare();

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
	
		sscanf(line, "%lld %lld", &a, &b);
		//printf("a=%lld, b=%lld\n", a, b);

		int count = 0;
		for (int j = 0; j < fairtbllen; j++)
		{
			if (b < fairtbl[j])
			{
				break;
			}
			if (a <= fairtbl[j] && b >= fairtbl[j])
			{
				count++;
			}
		}

		printf("Case #%d: %d\n", i+1, count);
	}

	
	fclose(f);
	return 0;
}
