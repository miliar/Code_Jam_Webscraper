/*
 * pancake.cpp
 *
 *  Created on: Apr 9, 2016
 *      Author: arup
 */
#include<stdio.h>
#include<string.h>

int main()
{
	char str[102];
	int test_case, i, j,k,len ,flip;
	freopen("pancake_in.txt","rt", stdin);
	freopen("pancake_out.txt","wt", stdout);
	scanf("%d",&test_case);
	for(i = 1; i <= test_case; i++)
	{
		getchar();
		scanf("%s", str);
		len = strlen(str);
		j = 0;
		flip = 0;
		if(len == 1)
		{
			if(str[0] == '-')
				flip = 1;
		}
		else
		{
			while(j != len-1)
			{
				while(str[j] == str[j+1] && j < len-1)
				{
					j++;
				}
				if(j<len-1) {
					flip++;
					for(k = 0; k <= j+1; k++)
						str[k] = str[j+1];
				}

			}
			if(str[len-1] == '-')
				flip++;
		}
		printf("Case #%d: %d\n",i,flip);
	}
	return 0;
}



