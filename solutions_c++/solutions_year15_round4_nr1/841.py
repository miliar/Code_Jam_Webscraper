/*
 * Pegman.cpp
 *
 *  Created on: May 30, 2015
 *      Author: jonathan
 */

#include <stdio.h>

int main()
{
	FILE* file,*out;
	file = fopen("A-large.in","r");
	out = fopen("A-large-out.txt","w");
	int num,i,j,k,ans,q,l,var,r,s,t;
	char a;
	fscanf(file,"%d",&num);
	for (i=0;i<num;i++)
	{
		fscanf(file,"%d",&j);
		fscanf(file,"%d",&k);
		int** grid = new int*[j];
		for(l = 0; l < j; l++)
		    grid[l] = new int[k];
		var = 0;
		for (l=0;l<j;l++)
		{
			for (q = 0; q < k;q++)
			{
			fscanf(file," %c",&a);
			switch (a)
			{
			case '.': grid[l][q] = 0; break;
			case '^': grid[l][q] = 1; var++; break;
			case '>': grid[l][q] = 2; var++; break;
			case 'v': grid[l][q] = 3; var++; break;
			case '<': grid[l][q] = 4; var++; break;
			}
			}
		}
		int *point_cor = new int[var];
		int *pot_point_cor = new int[var];
		r = 0;
		for (l=0;l<j;l++)
		{
			for (q = 0; q < k;q++)
			{
				switch (grid[l][q])
				{
				case 1:
					point_cor[r] = 0;
					s = l;
					s--;
					while (s >= 0)
					{
						if (grid[s][q] != 0)
						{
							point_cor[r] = 1;
						}
						s--;
					}; r++; break;
				case 2:
					point_cor[r] = 0;
					s = q;
					s++;
					while (s < k)
					{
						if (grid[l][s] != 0)
						{
							point_cor[r] = 1;
						}
						s++;
					}; r++; break;
				case 3:
					point_cor[r] = 0;
					s = l;
					s++;
					while (s < j)
					{
						if (grid[s][q] != 0)
						{
							point_cor[r] = 1;
						}
						s++;
					}; r++; break;
				case 4:
					point_cor[r] = 0;
					s = q;
					s--;
					while (s >= 0)
					{
						if (grid[l][s] != 0)
						{
							point_cor[r] = 1;
						}
						s--;
					}; r++; break;
				}
			}
		}
		r = 0;
		for (l=0;l<j;l++)
		{
			for (q = 0; q < k;q++)
			{
				if (grid[l][q] != 0)
				{
				t = 0;
				pot_point_cor[r] = 0;
				for (s=0;s<j;s++)
				{
					if (grid[s][q] != 0)
					{
						t++;
					}
				}
				for (s=0;s<k;s++)
				{
					if (grid[l][s] != 0)
					{
						t++;
					}
				}
				if (t > 2)
				{
					pot_point_cor[r] = 1;
				}
				r++;
				}
			}
		}
		r = 1;
		for (l = 0;l < var;l++)
		{
			if (pot_point_cor[l] == 0)
			{
				r = 0;
			}
		}
		if (r == 0)
		{
			fprintf(out,"Case #%d: IMPOSSIBLE\n",i+1);
		} else {
			s = 0;
			for (l = 0;l < var;l++)
			{
				if (point_cor[l] == 0)
				{
					s++;
				}
			}
			fprintf(out,"Case #%d: %d\n",i+1,s);
		}
	}
}


