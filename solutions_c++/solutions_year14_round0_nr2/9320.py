#include "stdio.h"
 
int main()
{
	FILE *file,*file1;
	int T = 0;
	double C = 500.0, F = 4.0, X = 2000.0, time = 0, R = 2.0;
		fopen_s(&file, "I:\\B-small-attempt0.in", "r");
		fopen_s(&file1, "I:\\B-small-attempt0.out", "w");
	if (file != NULL){
		
		fscanf_s(file, "%d", &T, sizeof(T));
		
	}
	int i = 0;
	for (i = 0; i<T; i++)
	{
		time = 0;
		R = 2.0;
		fscanf_s(file, "%lf%lf%lf",&C,&F,&X);
		

		while (X>0)
		{
			if (X < C)
			{
				time += (X / R);
				X = 0;
				break;

			}

			if ((X / R)>(((X) / (R + F))) + (C / R))
			{
				time += C / R;
				R = R + F;
			}
			else
			{
				time += X / R;
				X = 0;

			}


		}
		fprintf_s(file1,"Case #%d:%f\n",i+1, time);
	}
	fclose(file);
	fclose(file1);
	
	
	return 1;


}