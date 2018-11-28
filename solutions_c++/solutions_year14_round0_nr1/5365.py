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
	//string inputFile="input.txt";
	string inputFile="A-small-attempt0.in";
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
		
		vector<int> nbrs1(4);
		vector<int> nbrs2(4);

		getline(ifs,line);
		sstr = stringstream("");
		sstr << line;
		int l1;
		sstr >> l1;
		//cout << l1 << endl;
		for(int i=0; i<4; i++){
			getline(ifs,line);
			sstr = stringstream("");
			sstr << line;
			if(i+1 == l1){
				sstr >> nbrs1[0] >> nbrs1[1] >> nbrs1[2] >> nbrs1[3];
				//cout << line << endl;
			}
		}
		getline(ifs, line);
		sstr = stringstream("");
		sstr << line;
		int l2;
		sstr >> l2;
		//cout << l2 << endl;
		for(int i=0; i<4; i++){
			getline(ifs,line);
			sstr = stringstream("");
			sstr << line;
			if(i+1 == l2){
				sstr >> nbrs2[0] >> nbrs2[1] >> nbrs2[2] >> nbrs2[3];
				//cout << line << endl;
			}
		}

		sort(nbrs1.begin(), nbrs1.end());
		sort(nbrs2.begin(), nbrs2.end());

		size_t i1=0, i2=0;
		int card = -1;
		int nb_card = 0;
		while(i1 < nbrs1.size() && i2 < nbrs2.size()){
			if(nbrs1[i1] == nbrs2[i2]){
				nb_card++;
				card = nbrs1[i1];
				i1++;
				i2++;
				continue;
			}
			if(nbrs1[i1] < nbrs2[i2]){
				i1++;
				continue;
			}
			if(nbrs1[i1] > nbrs2[i2]){
				i2++;
				continue;
			}
		}
		
		cout << "Case #" << c << ": ";
		if(nb_card == 1){
			cout << card;
		}else if(nb_card > 1){
			cout << "Bad magician!";
		}else{
			cout << "Volunteer cheated!";
		}
		cout << endl;

		ofs << "Case #" << c << ": ";
		if(nb_card == 1){
			ofs << card;
		}else if(nb_card > 1){
			ofs << "Bad magician!";
		}else{
			ofs << "Volunteer cheated!";
		}
		ofs << endl;
	}

	ofs.close(); //close output file
	return 0;
}