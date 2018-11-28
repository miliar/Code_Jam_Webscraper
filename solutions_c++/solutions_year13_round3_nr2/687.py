#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <cmath>
#include <functional>
#include <cstring>

int main(void)
{
	int size;
	FILE *input, *output;
	if((input = fopen("B-small-attempt0.in", "rt")) == NULL)
	{
		printf("input fopen err\n");
		return 0;
	}

	if((output = fopen("B-small-attempt0.out", "wt")) == NULL)
	{
		printf("output fopen err\n");
		return 0;
	}

	fscanf(input,"%d",&size);
	
	for( int i = 0 ; i < size ; i++ )
	{
		int x = 0 , y = 0;
		int tx, ty;
		char str[100000];
		int indx = 0;
		fscanf(input,"%d %d",&tx, &ty);
		memset(str, 0, 100000);

		for( ; tx != x || ty != y ; ) 
		{
			if( tx < x ){
				sprintf(str+indx,"EW");
				x--;
				indx+=2;
			}
			else if( tx > x ){
				sprintf(str+indx,"WE");
				x++;
				indx+=2;
			}

			if( ty < y ){
				sprintf(str+indx,"NS");
				y--;
				indx+=2;
			}
			else if( ty > y ){
				sprintf(str+indx,"SN");
				y++;
				indx+=2;
			}
		}
		//sprintf(str+indx,"\n");
		fprintf(output, "Case #%d: %s\n", i+1 , str);
	}
	return 0;
}