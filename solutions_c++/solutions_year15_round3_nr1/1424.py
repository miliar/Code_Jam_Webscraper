// Brattleship.cpp : Defines the entry point for the console application.
//

#include <stdio.h>


int main()
{
	int T, R, C, W;
	int i, j, k;

	FILE *inputFile, *outputFile;
	inputFile = fopen("A-large.in", "r");
	outputFile = fopen("OUTPUT.txt", "w");
	fscanf(inputFile, "%d", &T);



	//scanf("%d", &T);


	

	for (i = 1; i <= T; i++)
	{
		fscanf(inputFile, "%d%d%d", &R, &C, &W);

		//scanf("%d%d%d", &R, &C, &W);
		


		//if ()
		//{
		//	fprintf(outputFile, "Case #%d: %d\n", i, R + (W - 1) + 1);
		//	//printf("Case #%d: %d\n", i, R + (W - 1) + 1);
		//}
		//else if ()
		//{
		//	fprintf(outputFile, "Case #%d: %d\n", i, R + (W - 1));
		//	//printf("Case #%d: %d\n", i, R + (W - 1));
		//}
		//else
		//{
		//	fprintf(outputFile, "Case #%d: %d\n", i, (R)*(C / W) + (W - 1));
		//	//printf("Case #%d: %d\n", i, (R)*(C - 2 * (W - 1)) + (W - 1));
		//}





		if (C%W == 0)
		{


			fprintf(outputFile, "Case #%d: %d\n", i, R*(C / W) + (W - 1));

			//printf("Case #%d: %d\n", i, R*(C / W) + (W - 1));



		}
		else
		{


			fprintf(outputFile, "Case #%d: %d\n", i, R*(C / W) + (W));

			//printf("Case #%d: %d\n", i, R*(C / W) + (W));




		}





	}






	return 0;
}

