#include <iostream>
#include <ios>
#include <fstream>
#include <string>
#include <sstream>
#include <cstring>
#include <cstdlib>
#include <vector>

using namespace std;

double getMinTime(double c, double f, double x)
{
    double t = 0.0;
    double lastT = x / 2;
    int n = 0;
    while (1) {
        t = 0.0;
        for(int i = 1; i <= n; ++i) {
            t += c / (2 + (i - 1) * f);
        }
        t += x / (2 + n * f); 
        if(t > lastT) {
            break;
        }
        else {
            lastT = t;
            ++n;
        }
    }
    return lastT;
}

int main(int argc, char *argv[])
{
	if (argc < 2) {
		cout << "Missing arguments!" << endl;
		return -1;
	}

	ifstream inputFile(argv[1]);
	string outputFileName = string(argv[1]) + ".out";
	ofstream outputFile(outputFileName.c_str(), ios::out | ios::trunc);
	if (!inputFile || !outputFile) {
		cout << "Open file error" << endl;
		return -2;
	}
    outputFile.precision(7);
    string line;
    getline(inputFile, line);
	int caseNum = atoi(line.c_str());
	int i = 0; 
	while (i < caseNum) {
        getline(inputFile, line);
        double c, f, x;
        stringstream ss;
        ss.str(line);
        ss >> skipws >> c >> f >> x;
            
        double t = getMinTime(c, f, x);
        outputFile << "Case #" << ++i << ": " << fixed << t << endl;
	}
	outputFile.flush();
	inputFile.close();
	outputFile.close();
	return 0;
}
