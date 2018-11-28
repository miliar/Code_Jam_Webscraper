#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>

using namespace std;

const string FILE_NAME = "B-small-attempt0";

double cookies(double cookieforfarm, double cookieperfarm, double cookielimit, double cookiespend, double cookiepersec) {
	double last = cookielimit / cookiepersec;
	if((cookiespend+cookieforfarm) < cookielimit) {
		double next = cookieforfarm / cookiepersec + cookies(cookieforfarm, cookieperfarm, cookielimit, cookiespend+cookieforfarm, cookiepersec+cookieperfarm);
		return (last<next)?last:next;
	}
	return last;
}

int main () {
	int cnt;
	string c, f, x;
	string fin = FILE_NAME + ".in";
	ifstream infile(fin.c_str());
	string fout = FILE_NAME + ".out";
	ofstream outfile(fout.c_str());
	if(infile.is_open()) {
		infile >> cnt;
		for(int i=0; i<cnt; i++) {
			infile >> c >> f >> x;
			double d = cookies(strtod(c.c_str(), NULL), strtod(f.c_str(), NULL), strtod(x.c_str(), NULL), 0, 2);
			outfile.setf(ios::fixed,ios::floatfield);
			outfile.precision(7);
			outfile << "Case #" << i+1 << ": " << d << endl;
		}
		outfile.close();
		infile.close();
	} else {
		cout << "Unable to open file!" << endl;
	}
	return 0;
}