#include <iostream>
using namespace std;

int main()
{
	FILE *input, *output;
	input = fopen("B-large.in", "r");
	output = fopen("output_cookie.txt", "w");

	int T;
	fscanf(input, "%d", &T);

	for (int t=1; t<=T; ++t)
	{
		fprintf(output, "Case #%d: ", t);
		double c, f, x;
		fscanf(input, "%lf %lf %lf", &c, &f, &x);

		double produce = 2;
		double min_time = x/produce;
		double time = 0;
		
		while (1)
		{
			time += c/produce;
			produce += f;

			if (min_time > time+x/produce)
			{
				min_time = time+x/produce;
			}

			else
				break;
		}
		fprintf(output, "%.7lf\n", min_time);
	}

	fclose(input);
	fclose(output);
	return 0;
}