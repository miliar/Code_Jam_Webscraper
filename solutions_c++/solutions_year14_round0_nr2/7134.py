#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <iomanip>

int main(){
	using namespace std;
	ofstream ofile;
	ifstream ifile;

	ifile.open("B-large.in");
	ofile.open("output.txt");

	if (ifile.is_open()){
		string line;
		getline(ifile, line);
		int casen = stoi(line);

		for (int CASE = 0; CASE < casen; CASE++){
			getline(ifile, line);
			stringstream ss(line);
			string cstr, fstr, xstr;
			ss >> cstr;
			ss >> fstr;
			ss >> xstr;
			double c = stod(cstr);
			double f = stod(fstr);
			double x = stod(xstr);
			double persec = 2.0;
			double cookies = 0.0;
			double totaltime = 0.0;

			double potTime = x / persec;

			while (true){
				totaltime += c / persec;
				if (totaltime >= potTime){
					//potTime is quickest for sure
					break;
				}
				persec += f;
				if ((x / persec) + totaltime < potTime){
					potTime = totaltime + (x / persec);
				}
			}

			ofile << "Case #" << to_string(CASE + 1) << ": " << setprecision(10) << potTime << endl;
		}
	}

	ofile.close();
}