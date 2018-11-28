//This Code was written by Alexandre Boulch

//Stantard Template Library
#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

//This code uses Eigen library
//http://eigen.tuxfamily.org/
#include <Eigen/Dense>
using namespace Eigen;

//this code uses Boost for big integer
#include <boost/multiprecision/cpp_int.hpp>
using namespace boost::multiprecision;
typedef boost::multiprecision::uint1024_t bigint;

int main(){
	
	//Files
	//string inputFile="B-small-attempt0.in";
	string inputFile="B-large.in";
	//string inputFile="input.txt";
	string outputFile="output.txt";

	//open input file
	ifstream ifs(inputFile.c_str());
	
	//get number of cases
	string line;
	getline(ifs,line);
	stringstream sstr(line);
	int n_cases;
	sstr >> n_cases;

	//open output file
	ofstream ofs(outputFile.c_str());

	//iterate on the cases
	// !!! case idx starts at 1
	for(int c=1; c<=n_cases; c++){
		
		getline(ifs,line);
		sstr = stringstream("");
		sstr << line;
		double C,F,X;
		sstr >> C >> F >> X;

		double current_t_farm = 0;
		double previous_time = X /2.;
		int nf=0;
		while(true){
			double t_farm = C /(2+nf*F);
			double x_t = X /(2+(nf+1)*F);
			if(x_t+current_t_farm+t_farm >= previous_time){
				break;
			}
			current_t_farm += t_farm;
			previous_time = x_t + current_t_farm;
			nf++;
		}
		double time = current_t_farm+X /(2+nf*F);
		
		ofs << "Case #" << c << ": ";
		ofs << setprecision(15) << time;
		ofs << endl;
	}
	
	ofs.close(); //close output file
	return 0;
}