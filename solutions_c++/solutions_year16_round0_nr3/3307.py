#include <stdio.h>

int main()
{
	int ca;
	scanf("%d",&ca);
	int casenum = 0;
	for(int i=0;i<ca;i++)
	{
		int str[100];
		casenum ++;
		printf("Case #%d:\n",casenum);
		int length, object;
		scanf(" %d %d", &length, &object);
		
		int count_get = 0;
		for(int sequence = (1 << (length-2))-1; sequence >= 0; sequence--)
		{

			int tmp = sequence;
			str[0] = 1;
			str[length-1] = 1;
			for(int pointer = 1;pointer < length-1;pointer ++)
			{
				str[pointer] = tmp%2;
				tmp = tmp >> 1;
			}
			int all_flag = 1;
			int factors[10];
			for(int base = 2;base<=10;base++)
			{
				/*long long num = 0;
				for(int j = 0;j<length;j++)
				{
					num = num*base+ str[j];
				}*/
				int flag = 1;
				for(int k=2; k< 100;k++)
				{
					int num = 0;
					for(int j=0;j<length;j++)
					{
						num = (num*base + str[j])%k;
					}
					if(num == 0)
					{
						flag = 0;
						factors[base] = k;
						break;
					}
				}
				if(flag == 1)
				{
					all_flag =0;
					break;
				}
			}
			if(all_flag == 1)
			{
				count_get++;
				for(int j=0;j< length;j++)
				{
					printf("%d",str[j]);
				}

				for(int base = 2;base <=10;base++)
				{
					long long num = 0;
					/*for(int j = 0;j<length;j++)
					{
						num = num*base + str[j];
					}
					printf("  num: %lld", num);*/
					printf(" %d", factors[base]);
				}
				printf("\n");
				if(count_get == object)
				{
					return 0;
				}
			}

		}
		
	}
}