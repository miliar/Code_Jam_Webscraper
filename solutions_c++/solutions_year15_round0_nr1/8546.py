#include <stdio.h>

int main(int argc, char* argv[])
{
	int tc;	
	scanf("%d",&tc);

	for(int t = 1 ; t <= tc ; ++t)
	{
		int sMax;
		scanf("%d",&sMax);
		fgetc(stdin);

		char inNumber;
		int stand = 0;
		int need = 0;
		int tmp;

		for(int sLevel = 0; sLevel <= sMax ; ++sLevel)			
		{
			if( stand < sLevel)
			{
				tmp = (sLevel - stand);
				need += tmp;
				stand += tmp;
			}
			inNumber = fgetc(stdin);
			tmp = (inNumber - '0');
			stand += tmp;
		
		}

		printf("Case #%d: %d\n",t,need);
	}


	return 0;
}