#include<iostream>
#include<string>
#include <fstream>
#include <iomanip>   
#include<stack>
#include<queue>
#include<vector>
using namespace std;
const double times = 2.0;
 double F;

double culc(double c, double f, double x){
	double tx = 0, tc = 0,free;
	vector<double> dd;
	tx = x / times;
	tc = c / times;
	f = times + f;
	free = tx;
	dd.push_back(free);
	while (true){
			sort(dd.begin(), dd.end());
			if (dd.front() != free){
				return dd.front();
			}	
			tx = (x / f) + tc;
			tc += c / f;
			free =(tx);	
			f = f + F;
			dd.push_back(free);
	}
}



int main(){
	ifstream myfile;
	myfile.open("input.in");
	ofstream out;
	out.open("output.txt");
	int rot=0,counter = 0;
	myfile >> rot;
	double c=0.0, f=0.0, x=0.0;

	while (counter != rot){
		myfile >> c;
		myfile >> f;
		F = f;
		myfile >> x;
		x=culc(c, f, x);

		out << "Case #" << counter + 1 << ": ";
	
		
		out << setprecision(7) << fixed<< x << endl;
		counter++;
	}
	
	out.close();
}