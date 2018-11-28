#include<stdio.h>
#include<math.h>

int main(){
	FILE *fp, *fp2;
	fp = fopen("A-large.in", "r");
	fp2 = fopen("sheepOut.txt", "w");

	int testCases;
	fscanf(fp, "%d", &testCases);
//	printf("testCases = %d\n\n", testCases);

	int digitsUsed[10];

	

	for(int i = 0; i < testCases; i++){
		for(int j = 0; j < 10; j++)
			digitsUsed[j] = 0;
		
		int initNum;
		fscanf(fp, "%d", &initNum);
//		printf("Case #%d: initNum = %d\n", i + 1, initNum);

		if(initNum > 0)
		{
			int doItAgain = 1;
			double num = initNum;
	//		printf("Case #%d: num = %d\n", i + 1, num);
			int multiplier = 0;
			while(doItAgain == 1)
			{
				multiplier++;
	//			printf("Multiplier = %d\n", multiplier);
				num = 1.0 * initNum * multiplier;

				doItAgain = 0;
				
				double tempNum = num;
	//			printf("tempNum = %d\n", tempNum);
				while(tempNum != 0)
				{
					digitsUsed[(int) fmod(tempNum, 10)] = 1;
					tempNum = (tempNum - fmod(tempNum, 10)) / 10;
				//	printf("%d\n\n", tempNum);
				}
				for(int j = 0; j < 10; j++)
					if(digitsUsed[j] == 0)
					{
						doItAgain = 1;
	//					printf("do it again\n\n");
					//	break;
					}
				
				
			}
			
			fprintf(fp2, "Case #%d: %.f\n", i + 1, num);
		}
		else
			fprintf(fp2, "Case #%d: INSOMNIA\n", i + 1);
	}

	
	
	fclose(fp);
	fclose(fp2);

	return 0;
}