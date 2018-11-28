#include<iostream>
#include<string>
#include<fstream>
#include<string.h>
#include <sstream>
#include <iomanip>      // std::setprecision

using namespace std;
double time1=0;
long double baseTime;
long double buyFarmTime;
long double withFarmTime;
ofstream outfile("output1.out");

void func(long double c, long double f, long double x,long double base){
	 baseTime = x / base;
	 buyFarmTime = c / base;
	 base = base + f;
	 withFarmTime = x / base;
	if (baseTime <= buyFarmTime+withFarmTime){
		time1 = time1 + baseTime;
		outfile << std::setprecision(std::numeric_limits<double>::digits10 - 5)<<time1 << endl;
		return;
	}
	else{
		time1 = time1 + buyFarmTime;
		//func(c, f, x, base);
		while (baseTime > buyFarmTime + withFarmTime){
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
			}
		}
		
	}
}
int main(){
	ifstream myfile("qq.in");
	string line;
	int testCases;
	int  caseNum = 1;
	if (myfile.is_open())
	{
		getline(myfile, line);
		testCases = stoi(line);
		while (testCases!=0)
		{
			getline(myfile, line, ' ');
			stringstream temp;
			long double c;
			temp << std::setprecision(std::numeric_limits<double>::digits10 + 1);
			temp << line;
			temp >> c;
			getline(myfile, line, ' ');
			stringstream temp1(line);
			long double f;
			temp1 << std::setprecision(std::numeric_limits<double>::digits10 + 1);
			temp1 << line;
			temp1 >> f;
			getline(myfile, line);
			stringstream temp2(line);
			long double x;
			temp2 << std::setprecision(std::numeric_limits<double>::digits10 + 1);
			temp2 << line;
			temp2 >> x;

			time1 = 0;
			outfile << "Case #" << caseNum++ << ": ";

			func(c, f, x,2.0);
			
				testCases--;
		}
		myfile.close();
	}

	else cout << "Unable to open file";
	return 0;
}
