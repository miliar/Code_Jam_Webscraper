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
	string inputFile="B-small-attempt0.in";
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
	//for(int c=1; c<=2; c++){

		getline(ifs,line);
		sstr = stringstream("");
		sstr << line;
		int A,B,K;
		sstr >> A >> B >> K;
		cout << A << " " << B << " " << K << endl;

		
		/*if(std::min(A,B) <=K){
			cout << "Case #" << c << ": ";
			cout << (std::min(A,B)+1)*(std::min(A,B)+1);//0 case
			cout << endl;
			continue;
		}*/

		int nbr=0;
		for(int a=0; a<A; a++){
			for(int b=0; b<B; b++){
				if(int(b&a)>=K){continue;}
				nbr++;
			}
		}

		cout << nbr <<endl;

		ofs << "Case #" << c << ": ";
		ofs << nbr;
		ofs << endl;
	}
	
	ofs.close(); //close output file
	return 0;
}