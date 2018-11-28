#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;

void main()
{
	int T, i, k; double C, F, X;
	char line[50], digit[50];

	ifstream ifile("B-large.in");

	ifile.getline(line, 50);
	T = atoi(line);

	ofstream ofile("output.out");

	double time_prev, time_now = 0, time = 0;
	double c = 0, f, x, incr = 2;
	bool flag = true;
	int loop = 1;

	for (int testCase = 1; testCase <=T; testCase++)
	{
		ifile.getline(line, 50);

		for (i = 0, k = 0; line[i] != ' '; i++, k++)
		{
			digit[k] = line[i];
		}
		digit[k] = '\0';
		i++;
		C = atof(digit);

		for (k = 0; line[i] != ' '; i++, k++)
		{
			digit[k] = line[i];
		}
		digit[k] = '\0';
		i++;
		F = atof(digit);

		for (k = 0; line[i] != '\0'; i++, k++)
		{
			digit[k] = line[i];
		}
		digit[k] = '\0';
		X = atof(digit);

		//     <- - COOKIES TIME- ->

		flag = true;
		time_prev = X / 2, time_now = 0, time = 0;
		incr = 2, loop = 1;
		while (flag)
		{
		
			incr = 2;
			time_now = 0;
			for (int i = 0; i < loop; i++)
			{
				time_now += C / incr;
				incr += F;
			}
		
			time_now += X / incr;

			if (time_prev <= time_now)
				flag = false;
			else
				time_prev = time_now;

			loop++;
		}
		ofile << setprecision(7) << fixed;
		ofile << "Case #" << testCase << ": ";
		ofile <<time_prev<<endl;
	}
}
