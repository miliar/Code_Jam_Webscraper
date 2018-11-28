#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

int main(){
	using namespace std;
	ofstream ofile;
	ifstream ifile;

	ifile.open("B-small-attempt0.in");
	ofile.open("output.txt");

	if (ifile.is_open()){
		string line;
		getline(ifile, line);
		int casen = stoi(line);

		for (int CASE = 0; CASE < casen; CASE++){
			getline(ifile, line);
			stringstream ss(line);
			string astr;
			string bstr;
			string kstr;
			ss >> astr;
			ss >> bstr;
			ss >> kstr;

			int a = stoi(astr);
			int b = stoi(bstr);
			int k = stoi(kstr);
			int total = 0;
			for (int an = 0; an < a; an++){
				for (int bn = 0; bn < b; bn++){
					if ((an&bn) < k){
						total++;
					}
				}
			}

			ofile << "Case #" << to_string(CASE + 1) << ": " << total << endl;
		}
	}

	ofile.close();
}