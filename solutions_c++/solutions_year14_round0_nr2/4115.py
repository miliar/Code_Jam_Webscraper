#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <iomanip>
using namespace std;
int main() {
	ifstream myfile("B-large.in");
	ofstream outfile;
	outfile.open ("result.txt");
	string data;
	int T, c = 1;;
	double X, C, F, bestTime;
	getline(myfile, data);
	stringstream(data)>>T;
	do {
		getline(myfile, data);
		istringstream stream(data);
		stream >> C >> F >> X;
		double temp, Farm=0;
		Farm = C/2;
		bestTime = X/2;
		temp = Farm + X/(2+F);
		int count = 1;
		while(temp < bestTime) {
			bestTime = temp;
			Farm = Farm + C/(2+count*F);
			temp = Farm + X/(2+(count+1)*F);
			count++;
		}
	
		outfile<< fixed << setprecision(7) << showpoint <<"Case #"<<c<<": "<<bestTime<<"\n";
		c++;
		T--;
	} while(T!=0);
	outfile.close();
	return 0;
}
