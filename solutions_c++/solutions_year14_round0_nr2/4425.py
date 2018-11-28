#include <iostream>

int main()
{
	
	//FILE* file = fopen("C:\\Users\\RezaulAkram\\Desktop\\B-large.in","r");;
	//FILE* opfile = fopen("C:\\Users\\RezaulAkram\\Desktop\\opfile.txt","w");

	FILE* file = stdin;
	FILE* opfile = stdout;

	int T = 0;
	fscanf(file, "%d",&T);

	for(int i = 0 ; i < T; i++)
	{
		double C =0, F = 0, X = 0;
		double init = 2.0, currentSpeed = 2.0;
		fscanf(file, "%lf %lf %lf", &C, &F, &X);

		if(X > C)
		{
			double timetaken = 0;
			while(((X-C)/ currentSpeed) > (X/ (currentSpeed + F)))
			{
				timetaken += (C / currentSpeed);
				currentSpeed += F;
			}

			timetaken += (X/ currentSpeed);

			fprintf(opfile,"Case #%d: %.7f\n", i+1, timetaken);
		}
		else
		{
			double timetaken = X / 2.0;
			fprintf(opfile, "Case #%d: %.7f\n", i+1, timetaken);
		}
	}
}