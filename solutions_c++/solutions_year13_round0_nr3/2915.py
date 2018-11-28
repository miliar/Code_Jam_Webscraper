#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string>

int main(int argc , char * argv[])
{
	int T;
	scanf("%d",&T);
	for(int t = 0;t<T;t++)
	{
		int A;
		int B;
		scanf("%d %d",&A,&B);
		char val[5];
		int count = 0;

		for(double i = A;i<=B;i++)
		{
			bool che = true;
			int I = i;
			sprintf(val,"%d",I);
			char * end = val + strlen(val);
			char * ptr = val;
			char * ptr2 = end-1;
			for(ptr , ptr2 ; ptr < end ;ptr++,ptr2--)
			{
				if(*ptr != *ptr2)
				{
					che = false;
				}
			}
			bool che2 = true;
			int NEI = 0;
			if(che == true)
			{
				double nei = sqrt(i);
				NEI = nei;
				if(nei-NEI != 0)
				{
					che2 = false;
				}
			}
			bool che3 = true;
			if(che2 == true && che == true)
			{
				sprintf(val,"%d",NEI);
				char * end = val + strlen(val);
				char * ptr = val;
				char * ptr2 = end-1;
				for(ptr , ptr2 ; ptr < end ;ptr++,ptr2--)
				{
					if((*ptr) != (*ptr2))
					{
						che3 = false;
					}
				}
			}
			if(che3 == true && che2 == true && che == true)
			{
				count++;
			}
		}
		printf("Case #%d: %d\n",(t+1),count);
	}

	return 0;
}