#include<stdio.h>
typedef struct count {
	unsigned int number[10];
	unsigned int flag[10];
};
void main()
{
	int T,i,flagcount=0;
	unsigned int data,stacticdata;
	unsigned int last,flagnumber;
	FILE * fp = fopen("output.in", "w");
	count tmp;
	scanf("%d", &T);
	for (i = 0; i < T; i++)//케이스 개수
	{
		for (int j = 0; j < 10; j++)//초기화, 플래그 
		{
			tmp.number[j] = j;
			tmp.flag[j] = 0;
		}

		scanf("%u", &data);//자료값 입력
		stacticdata = data;
		//last=data;
		while(1)
		{
			last = data;
			if (data == 0)//0이면 와일빠져나감
			{
				break;
			}
			for (int k = 0; ;k++)//자리수 별로 추출 한뒤 number비교후 증가 flag
			{
				
				flagnumber= last % 10;//라스트만 이용해서 계산.
				last = last / 10;
				for (int l = 0; l < 10; l++)
				{
					if (flagnumber == tmp.number[l])
					{
						tmp.flag[l] = 1;
					}
				}
				if (last == 0) break;
			}
			for (int l = 0; l < 10; l++)
			{
				if (1 == tmp.flag[l])
				{
					flagcount++;
				}
			}
			if (flagcount == 10)
			{
				break;
			}
			data = data + stacticdata;//N*2
			flagcount = 0;
		}
		if (data == 0)
		{
			printf("Case #%d: INSOMNIA\n", i + 1);
			fprintf(fp, "Case #%d: INSOMNIA\n", i + 1);
		}
		else
		{
			printf("Case #%d: %u\n", i + 1, data);
			fprintf(fp, "Case #%d: %u\n", i + 1, data);
		}
		flagcount = 0;
	}
}