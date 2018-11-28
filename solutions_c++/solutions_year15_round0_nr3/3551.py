#include <stdio.h>
#include <stdlib.h>
#include <string>
			  //    1    i   j   k
int map[5][5] = {0 , 0 , 0 , 0 , 0,
		/* 1 */	 0 , 1 , 2 , 3 , 4,    
		/* i */	 0 , 2 ,-1 , 4 ,-3,   
		/* j */	 0 , 3 ,-4, -1 , 2,    
		/* k */	 0 , 4 , 3, -2 ,-1 };  

int main()
{
	FILE *fp;
	FILE *fp_result;

	fp = fopen("C-small-attempt4.in", "r");
	fp_result = fopen("C-test-result.in", "w");


	int T;
	fscanf(fp, "%d\n", &T);
	int numofcase = 1;
	while(T--)
	{
		int L, X;
		fscanf(fp, "%d %d\n", &L, &X);
		char small_str[10050] = {NULL, };
		char str[10050] = {NULL, };
		fscanf(fp, "%s\n", small_str);

		for(int i = 0; i < X; i++)
		{
			strcat(str, small_str);
		}

		
		if(L == 1)
		{
			fprintf(fp_result, "Case #%d: NO\n", numofcase++);
			continue;
		}
		if(L * X < 3)
		{
			fprintf(fp_result, "Case #%d: NO\n", numofcase++);
			continue;
		}

		int cur = 0;
		bool negative = false;
		char target = 'i';

		while(str[cur] != '\0')
		{
			if(str[cur] == target)
			{
				target++;
				cur++;
			}
			else
			{
				if(str[cur+1] == '\0')
				{
					if(str[cur] != 'h')
					{
						target--;
					}
					break;
				}

				cur++;
				int tmp = map[str[cur-1] - 'g'][str[cur] - 'g'];
				if(tmp < 0)
				{
					negative ^= true;
					tmp *= -1;
				}
				str[cur-1] = '0';
				str[cur] = tmp + 'g';
			}
		}
			

		if(target == 'l' && negative == false)
		{
			fprintf(fp_result, "Case #%d: YES\n", numofcase++);
		}
		else
		{
			fprintf(fp_result, "Case #%d: NO\n", numofcase++);
		}
	}

	fclose(fp);
	fclose(fp_result);
}