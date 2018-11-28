#include "stdafx.h"
#include <stdlib.h>
#define MAX_Pancake 9 

int main(int argc, char* argv[])
{
	int t,d,p[2000],p_temp[2000];
	int temp;
	int i, j, k;
	int minute,pre_minute,end_minute,max_minute,max_minute_temp;
	int move;
//	bool flag;
//	bool cheat;
	FILE *IN, *OUT;
	IN = fopen ("B-small-attempt4.in" , "r");
	OUT = fopen ("B-small-attempt4.out" , "w");
//	scanf("%d", &t);
	fscanf(IN, "%d", &t);
	for(i=0; i<t; i++)
	{
//		flag = false;
//		cheat = false;
		end_minute = 1001;
		pre_minute = 1001;
		minute = 0;
		max_minute = 0;
		move = 0;

		fscanf(IN, "%d", &d);
//		printf("%d\n",d);
//		fprintf(OUT, "%d\n",d);
/*		if(d == 1)
			cheat = true;*/
		for(j=0; j<=MAX_Pancake; j++)
		{
			p[j] = 0;
			p_temp[j] = 0;
		}
		for(j=0; j<d; j++)
		{
			fscanf(IN, "%d",&temp);
//			printf("%d ", temp);
//			fprintf(OUT, "%d ", temp);
//			p_temp[temp]++;
			p[temp]++;
		}
//		printf("\n");
//		fprintf(OUT, "\n");

		for(j=MAX_Pancake; j>0; j--)
			if(p[j]!=0)
			{
				max_minute = j;
				break;
			}
/*		if(cheat == true && p[9] == 1)
		{
			printf("%d-\n",5);
			fprintf(OUT, "-Case #%d: %d\n\n", i+1, 5);
			continue;
		}*/
/*		for(j=MAX_Pancake; j>0; j--)
		{
			minute = j + move;
			if(p[j] == 0)
				continue;
			else
			{
				if (minute > pre_minute)
				{}//break;
				else 
					pre_minute = minute;

/*				if(flag == false)
				{
					pre_minute = j;
					flag = true;
				}
				else{}*/
				
/*				if(j % 2 == 0)
					p[j/2] = p[j/2] + p[j] * 2;
				else
				{
					p[j/2+1] = p[j/2+1] + p[j];
					p[j/2] = p[j/2] + p[j];
				}
				move = move + p[j];
				if(move > pre_minute)
					break;
			}
		}*/
//		end_minute = pre_minute;

		//------------------------------------------

		for(j=2; j<=(MAX_Pancake/2); j++){
			for(k=0;k<=9;k++)
				p_temp[k] = p[k];
 			move = 0;
			pre_minute = max_minute;
			max_minute_temp = max_minute;
			for(k=max_minute_temp; k>=j+1; k--){
				move = move + p_temp[k];
				p_temp[k-j] = p_temp[k-j] + p_temp[k];
				max_minute_temp--;
				minute = move + max_minute_temp;
				if (minute < pre_minute)
					pre_minute = minute;
			}
			if(pre_minute < end_minute)
				end_minute = pre_minute;
		}

		printf("%d\n",end_minute);
		fprintf(OUT, "Case #%d: %d\n\n", i+1, end_minute);
	}

	system("pause");
	return 0;
}

