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

		getline(ifs,line);
		sstr = stringstream("");
		sstr << line;
		int nstring;
		sstr >> nstring;
		//cout << "nstring: " << nstring << endl;

		vector<string> strings(nstring);
		for(int s=0; s<nstring; s++){
			getline(ifs,strings[s]);
		}

		vector<int> moves(nstring,0);
		vector<int> pos(nstring,0);

		int total_moves = 0;
		bool go_on = true;

		while(true){

			char letter = '1';
			for(int s=0; s<nstring; s++){
				if(pos[s] < strings[s].size()){
					letter = strings[s][pos[s]];
				}
			}
			if(letter == '1'){
				break;
			}
			vector<int> nbrs(nstring,0);
			for(int s=0; s<nstring; s++){
				if(strings[s][pos[s]] != letter){
					go_on = false;
					break;
				}
				int nidentical=0;
				while(pos[s]+nidentical+1<strings[s].size() && strings[s][pos[s]] == strings[s][pos[s]+nidentical+1]){
					nidentical++;
				}
				nbrs[s] = nidentical+1;
				pos[s] += nidentical+1;
				//cout << nidentical << " " << pos[s]<< endl;
			}
			if(!go_on){
				break;
			}
			sort(nbrs.begin(), nbrs.end());
			int nref = nbrs.front();
			int n_moves_min = 1e7;
			do{
				int nmoves = 0;
				for(int i=0; i<nbrs.size(); i++){
					nmoves += abs(nref - nbrs[i]);
				}
				if(n_moves_min > nmoves){
					n_moves_min = nmoves;
				}else{
					break;
				}
				nref++;
			}
			while(nref!=nbrs.back());
			total_moves += n_moves_min;
			//cout << "** " << n_moves_min << endl;
			//cout << "--" << endl;
		}

		cout << "Case #" << c << ": ";
		if(!go_on){
			cout << "Fegla Won";
		}else{
			cout << total_moves;
		}
		cout << endl;

		ofs << "Case #" << c << ": ";
		if(!go_on){
			ofs << "Fegla Won";
		}else{
			ofs << total_moves;
		}
		ofs << endl;
	}

	ofs.close(); //close output file
	return 0;
}