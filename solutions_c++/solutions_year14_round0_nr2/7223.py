#include <iostream>
#include <fstream>
#include <string>

#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <vector>
#include <map>
#include <algorithm>
#include <assert.h>


#include <math.h>

using namespace std;

vector<double> strTodoubleVector(string v);

class CookieManager {
	private:
		double rate;
		double C;
		double F;
		double X;
		double cookieCount;

	public:

		CookieManager(string line, double cookieCount) {
			vector<double> CFX = strTodoubleVector(line);
			//int i;
			//for (i = 0; i < CFX.size(); i++) {
			//	cout << CFX[i] << " ";
			//}
			//cout << endl;
			C = CFX[0];
			F = CFX[1];
			X = CFX[2];
			this->cookieCount = cookieCount;
			rate = 2.0;
		}

		double getTimeToReachTarget(double target) {
			double time = (target - cookieCount)/rate;
			return time;
		}

		double getTimeToOvertake(CookieManager other) {
			double rDiff = this->getRate() - other.getRate();
			double countDiff = other.getCookieCount() - this->getCookieCount();
			return countDiff/rDiff;
		}

		double getTimeToVictory() {
			if (X < C) {
				//cout << "X=" << X << " F=" << F << endl;
				return X/rate;
			}
			else {
				double time = getTimeToReachTarget(C);
				this->setCookieCount(C);
				CookieManager clone = *this;
				clone.buyCookieFarm();

				double timeToGoal = this->getTimeToReachTarget(X);

				while (clone.getTimeToOvertake(*this) < timeToGoal) {
					this->buyCookieFarm();
					time += getTimeToReachTarget(C);
					this->setCookieCount(C);
					clone = *this;
					clone.buyCookieFarm();
					timeToGoal = getTimeToReachTarget(X);
				}

				time += getTimeToReachTarget(X);
				return time;
			}
		}

		void buyCookieFarm() {
			cookieCount -= C;
			rate += F;
		}
		
		double getF() {
			return F;
		}
		
		double getRate() {
			return rate;
		}

		double getCookieCount() {
			return cookieCount;
		}
		
		void setCookieCount(double cookieCount) {
			this->cookieCount = cookieCount;
		}	
};


vector<CookieManager> readFile(char* filename) {
	vector<CookieManager> cases;
	ifstream infile(filename);
	string line;

	if (infile.is_open()) {
		getline(infile,line);
		int r, c, t, T = atoi(line.c_str());
		vector<double> CFX;
		
		for (t = 0; t < T; t++) {
			getline(infile,line);
			CookieManager cManager(line, 0);
			cases.push_back(cManager);
		}

		infile.close();
	}
	else { 
		perror("open"); 
	}

	return cases;
}

vector<double> strTodoubleVector(string v) {
	vector<double> vec;
	char pointer[strlen(v.c_str()) + 1];
	strcpy(pointer, v.c_str());

	const char* space = " ";
	char* dim = strtok(pointer, space);
	while (dim) {
		vec.push_back((double) atof(dim));
		dim = strtok(NULL, space);
	}
	return vec;
}

int main(int argc, char** argv) {
	vector<CookieManager> cases = readFile(argv[1]);
	int i;
	for (i = 0; i < cases.size(); i++) {
		CookieManager cManager = cases[i];
		printf("Case #%d: %f\n", i+1, cManager.getTimeToVictory());
	}
}












