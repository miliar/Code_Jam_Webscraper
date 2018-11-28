#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <algorithm>

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	
	int T;
	scanf("%d", &T);
	
	for(int t = 1; t <= T; t++)
	{
		int n;
		scanf("%d", &n);
		
		char str[200], id[200], cur_id[200];
		int num[200][200] = {0}, sum = 0, len = 0;
		bool fegla = false;
		
		for(int i = 0; i < n && !fegla; i++)
		{
			scanf("%s", str);
			int k = -1;
			
			for(int j = 0; j < strlen(str); j++)
				if(j > 0 && str[j] == str[j - 1])
				{
					//cur_id[k] = str[j];
					num[i][k]++;	
				}
				else
				{
					k++;
					cur_id[k] = str[j];
					num[i][k]++;
				}
			
			if(i == 0)
				len = k;
			else
				if(len != k)
				{
					fegla = true;
					break;
				}
			
			for(int j = 0; j <= k; j++)
				if(i == 0)
					id[j] = cur_id[j];
				else
					if(cur_id[j] != id[j])
						fegla = true;
		}
		
		for(int i = 0; i <= len && !fegla; i++)
		{
			int tmp[200], p = 0;
			
			for(int j = 0; j < n; j++)
				tmp[p++] = num[j][i];
				
			std::sort(tmp, tmp + p);
			/*for(int j = 0; j < p; j++)	
				printf("%d ", tmp[j]);
			printf("\n");*/
			
			for(int j = 0; j < p; j++)
				sum += abs(tmp[j] - tmp[p / 2]);
		}
		
		if(fegla)
			printf("Case #%d: Fegla Won\n", t);
		else
			printf("Case #%d: %d\n", t, sum);		
	}
	return 0;
}

