#include <stdio.h>
#include <math.h>

#include <vector>
#include <iostream>
#include <sstream>
#include <cmath>
#include <iomanip> 

using namespace std;

#define MAX_BUFFER 1024
#define INITIAL_COOKIE_SPEED 2.00
#define DECIMALS 7

double roundf(double val, int precision)
{
    std::stringstream s;
	s << std::fixed << std::setw(10) << std::setprecision(precision) << val;

    //s << std::setprecision(precision) << std::setiosflags(std::ios_base::fixed)<< val;
    s >> val;
    return val;
}

double truncate(double &d, unsigned int numberOfDecimalsToKeep)
{
    return roundf(d, numberOfDecimalsToKeep);
}

void readData(FILE *f, float *C, float *F, float *X)
{
	fscanf_s(f, "%f", &(*C));
	if (*C<1.00 || *C>500.00)
	{
		printf("1 <= C <= 500.");
		exit(-1);
	}
	
	fscanf_s(f, "%f", &(*F));
	if (*F<1.00 || *F>4.00)
	{
		printf("1 <= F <= 4!");
		exit(-1);
	}

	fscanf_s(f, "%f", &(*X));
	if (*C<1.00 || *C>2000.00)
	{
		printf("1 <= X <= 2000.");
		exit(-1);
	}
}

void printTotalTime(double totalTime,std::string &output)
{	
	char str[MAX_BUFFER] = {0};
	sprintf_s(str, "%.7f", totalTime);
	output.append(str);
}

void writePretext(int i, std::string &output)
{
	char str[MAX_BUFFER] = {0};

	output.assign("Case #");
	
	sprintf_s(str, "%d", i);
	output.append(str);
	
	output.append(": ");
}

void buyFarm(float C, float F, double *totalCookies, double *cookieSpeed)
{
	*totalCookies = *totalCookies - C;
	*cookieSpeed += F;
}

void increaseCookies(double cookieSpeed, double *totalCookies)
{
	*totalCookies = *totalCookies + cookieSpeed;
}

double getTimeToXbyBuyingAFarm(float C, float F, float X, double cookieSpeed)
{
	double possibleCookieSpeed = cookieSpeed + F;
	return (double)X/possibleCookieSpeed + (double)C/cookieSpeed;
}

double getTimeToXByCurrentSpeed(float X, double cookieSpeed)
{
	return (double)X/cookieSpeed;
}

bool shouldBuyFarm(float C, float F, float X, double cookieSpeed, double *timeToXbyCurrentSpeed)
{
	double timeToXbyBuyingAFarm = getTimeToXbyBuyingAFarm(C, F, X, cookieSpeed);
	*timeToXbyCurrentSpeed = getTimeToXByCurrentSpeed(X, cookieSpeed);
		
	if (*timeToXbyCurrentSpeed > timeToXbyBuyingAFarm)
		return true;

	return false;
}

double solve(double initialCookieSpeed, float C, float F, float X)
{
	double cookieSpeed = (double)initialCookieSpeed;
	double totalCookies = 0;
	double time = 0.0;
	int nrFarms = 0;
	
	while (true)
	{
		double timeToXbyCurrentSpeed = 0.0;
		increaseCookies(cookieSpeed, &totalCookies);

		if (shouldBuyFarm(C, F, X, cookieSpeed, &timeToXbyCurrentSpeed))
		{
			if (totalCookies >= C)
			{
				time += (double)C/cookieSpeed;
				time  = truncate(time, DECIMALS);
				buyFarm(C, F, &totalCookies, &cookieSpeed);
				nrFarms++;
			}
		}
		else
		{
			//win & stop timer
			if (totalCookies >= X)
			{
				time += timeToXbyCurrentSpeed;
				//time = truncate(time, DECIMALS);
				break;
			}
		}
	}

	return time;
}

int main(int argc, char **argv)
{
	// input variables 
	int T = 0;
	FILE *fin = NULL;
	FILE *fout = NULL;
	const char *filename_in = argv[1];
	const char * filename_out = "out.txt";

	// output variables
	std::string output;
	
	fopen_s(&fin, filename_in, "r");
	if (fin == NULL)
	{
		printf("Could not open file %s\n", filename_in);
		exit(-1);
	}

	fopen_s(&fout, filename_out, "w+");
	if (fout == NULL)
	{
		printf("Could not open file %s\n", filename_out);
		exit(-1);
	}

	fscanf_s(fin, "%d", &T);

	if (T < 1 || T > 100)
	{
		printf("1 <= T <= 100!");
		exit(-1);
	}

	for (int i = 1; i <= T; i++)
	{
		float C, F, X = 0.0;
		double totalTime = 0.0;
		readData(fin, &C, &F, &X);
	
		writePretext(i, output);

		totalTime = solve(INITIAL_COOKIE_SPEED, C, F, X);
		
		printTotalTime(totalTime, output);

		fprintf(fout, "%s\n", output.c_str());
	}

	fclose(fin);
	fclose(fout);

	return 0;
}
