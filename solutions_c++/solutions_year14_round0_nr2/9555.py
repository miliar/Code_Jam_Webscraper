#include<iostream>
#include<string>
#include<fstream>
#include<string.h>
#include <sstream>
#include <iomanip>      // std::setprecision

using namespace std;
double time1 = 0;
double baseTime;
double buyFarmTime;
double withFarmTime;
ofstream outfile("output.out");

void func(double c, double f, double x, double base){
	baseTime = x / base;
	buyFarmTime = c / base;
	base = base + f;
	withFarmTime = x / base;
	if (baseTime < buyFarmTime + withFarmTime){
		time1 = time1 + baseTime;
		outfile << std::setprecision(std::numeric_limits<double>::digits10 - 5) << time1 << endl;
		return;
	}
	else{
		time1 = time1 + buyFarmTime;
		func(c, f, x, base);
	}
}
int main(){
	ifstream myfile("B-small-attempt1.in");
	string line;
	int testCases;
	int  caseNum = 1;
	if (myfile.is_open())
	{
		getline(myfile, line);
		testCases = stoi(line);
		while (testCases != 0)
		{
			getline(myfile, line, ' ');
			stringstream temp;
			double c;
			temp << std::setprecision(std::numeric_limits<double>::digits10 + 1);
			temp << line;
			temp >> c;
			getline(myfile, line, ' ');
			stringstream temp1(line);
			double f;
			temp1 << std::setprecision(std::numeric_limits<double>::digits10 + 1);
			temp1 << line;
			temp1 >> f;
			getline(myfile, line);
			stringstream temp2(line);
			double x;
			temp2 << std::setprecision(std::numeric_limits<double>::digits10 + 1);
			temp2 << line;
			temp2 >> x;

			time1 = 0;
			outfile << "Case #" << caseNum++ << ": ";
			func(c, f, x, 2.0);

			testCases--;
		}
		myfile.close();
	}

	else cout << "Unable to open file";
	return 0;
}
