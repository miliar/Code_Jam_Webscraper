#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
	FILE *fp;
	char buff[1024];
	int m1[4][4], m2[4][4];
	int t, x, a1, a2, r, c, z, i, j;

	fp = fopen(argv[1], "r");

	if (!fp) return (-1);

	t = atoi(fgets(buff, sizeof(buff), fp));

	for(x=1;x<=t;x++)
	{
		a1 = atoi(fgets(buff, sizeof(buff), fp));

		for (r=0;r<4;r++)
		{
			fgets(buff, sizeof(buff), fp);
			sscanf(buff, "%d %d %d %d", &m1[r][0], &m1[r][1], &m1[r][2], &m1[r][3]); 
		}

		a2 = atoi(fgets(buff, sizeof(buff), fp));

		for (r=0;r<4;r++)
		{
			fgets(buff, sizeof(buff), fp);
			sscanf(buff, "%d %d %d %d", &m2[r][0], &m2[r][1], &m2[r][2], &m2[r][3]); 
		}

		z = 0;

		for (i=0;i<4;i++)
		{
			for (j=0;j<4;j++)
			{
				if (m1[a1-1][i] == m2[a2-1][j])
				{
					c = j;
					z++;
				}
			}
		}

		if (z == 0)
		{
			printf("Case #%d: Volunteer cheated!\n", x);
		}
		else if (z == 1)
		{
			printf("Case #%d: %d\n", x, m2[a2-1][c]);
		}
		else if (z > 1)
		{
			printf("Case #%d: Bad magician!\n", x);
		}

	}
	
	fclose(fp);
	return (0);
}
