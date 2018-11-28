#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>

using namespace std;

double findTime(double c, double f, double x, double ii, double ut)
{
	if (ut+(x/ii) < ut+(c/ii)+(x/(ii+f)))
		return ut+(x/ii);
	else
		return findTime(c, f, x, ii+f, ut+(c/ii));
}

int main(int argc, char *argv[])
{
	FILE *fp;
	char buff[1024];
	int t, i;
	double c, f, x, y, z, w, ty;

	if (!(fp = fopen(argv[1], "r"))) return (-1);

	t = atoi(fgets(buff, sizeof(buff), fp));

	for(i=1;i<=t;i++)
	{
		fgets(buff, sizeof(buff), fp);
		sscanf(buff, "%lf %lf %lf", &c, &f, &x);

		y = findTime(c, f, x, 2.0, 0.0);

		printf("Case #%d: %.7f\n", i, y);
	}
	
	fclose(fp);
	return (0);
}
