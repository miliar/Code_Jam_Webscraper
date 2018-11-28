/*
 * omino.cpp
 *
 *  Created on: 11-Apr-2015
 *      Author: porichar
 */

#include <iostream>
#include <stdio.h>
using namespace std;

int min_t(int x)
{
	if (0 == x%2)
	{
		return (x/2);
	}
	else
	{
		return  (x+1)/2;
	}
}


int main ()
{
	int loop = 1;
	scanf("%d",&loop);
	FILE *f = fopen("/home2/porichar/pop/g/out/omino.txt", "a+");
	for(int i_loop=1 ;i_loop <=loop ; i_loop++)
	{
		int x,r,c;
		cin >>x>>r>>c;
		if(x==1)
		{
			fprintf(f,"Case #%d: GABRIEL\n", i_loop);
		}
		else if (min_t(x) > r)
		{
			fprintf(f,"Case #%d: RICHARD\n", i_loop);
		}
		else if (min_t(x) > c)
		{
			fprintf(f,"Case #%d: RICHARD\n", i_loop);
		}
		else if ((x>3) && ((min_t(x) == r) || (min_t(x) == c)))
		{
			fprintf(f,"Case #%d: RICHARD\n", i_loop);
		}
		else
		{
			if (x>6)
			{
				fprintf(f,"Case #%d: RICHARD\n", i_loop);
			}
			else if ((((r*c) - x) % x) == 0)
			{
				fprintf(f,"Case #%d: GABRIEL\n", i_loop);
			}
			else
			{
				fprintf(f,"Case #%d: RICHARD\n", i_loop);
			}
		}
	}
	fclose(f);
	return 0;
}

