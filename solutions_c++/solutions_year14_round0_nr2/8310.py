#include <cstdlib> //atoi
#include <fstream> //reading files, writing to files
#include <iomanip> //fixing and setting the precision of doubles
#include <iostream>
#include <string>
#include <sstream>

using std::cout;
using std::endl;
using std::fixed;
using std::ifstream;
using std::ofstream;
using std::setprecision;
using std::string;
using std::stringstream;

const double RATE = 2.0;

int getNumTrials(ifstream &input);
void getParams(double &farmPrice, double &rateBoost, double &cookieCount, ifstream &input);

double finishTime(double rate, double endCookies);
double farmTime(double rate, double fPrice);
void resultOut(ofstream &output, int trialNum, double time);

int main()
{
	double rate;

	ifstream input("input.txt");
	ofstream output("output.txt");
	int numTrials = getNumTrials(input);
	double farmPrice, rateBoost, cookieCount;
	
	int count = 0;
	double totalTime;
	double finishNow;
	double finishLater = 100000;

	while (count < numTrials) {
		//getting the parameters from the file
		getParams(farmPrice, rateBoost, cookieCount, input);
		//(re)setting time and rate
		totalTime = 0.0;
		rate = RATE;		
		do {
			finishNow = totalTime + finishTime(rate, cookieCount);
			finishLater = totalTime + farmTime(rate, farmPrice) + finishTime(rate + rateBoost, cookieCount);
			totalTime += farmTime(rate, farmPrice);
			rate += rateBoost;
		} while (finishLater < finishNow);
		resultOut(output, ++count, finishNow);	
	}		
	return 0;
}

double finishTime(double rate, double endCookies)
{
	return (endCookies / rate);
}

double farmTime(double rate, double fPrice)
{
	return (fPrice / rate);
}

int getNumTrials(ifstream &input)
{
	string temp;
	int numTrials;
	getline(input, temp);
	//convert temp to a c string then to an integer
	numTrials = atoi(temp.c_str());
	return numTrials;
}

void getParams(double &farmPrice, double &rateBoost, double &cookieCount, ifstream &input)
{
	string temp;
	stringstream line;
	getline(input, temp);
	line << temp;
	line >> farmPrice >> rateBoost >> cookieCount;
}

void resultOut(ofstream &output, int trialNum, double time)
{
	output << "Case #" << fixed << setprecision(7) << trialNum << ": " << time << endl;
}
