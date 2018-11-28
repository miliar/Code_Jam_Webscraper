#include <iostream>
#include <thread>
#include <string>
#include <exception>
#include <fstream>
#include <vector>
#include <boost/algorithm/string.hpp>
#include <sstream>

using namespace std;

void inputfileReader(vector<string> *com, string *input){
	ifstream in(*input);
	string temp;

	if (in.is_open()) {
		while(in.good()){
			getline(in, temp);
			com->push_back(temp);
		}
		in.close();
	} else {
		cout<<"Unable to read file"<<endl;
	}
}

void outputfileWriter(vector<string> *res, string *output){
	ofstream out(*output);

	if (out.is_open()) {
		for (unsigned i = 0; i < res->size(); i++) {
			if (i != 0) {
				out<<endl;
			}
			out <<"Case #"<<i+1<<": "<<res->at(i);
		}
		out.close();
	} else {
		cout<<"Unable to write file"<<endl;
	}
}

void Problem_A_Tic_Tac_Toe_Tomek(vector<string> *com, vector<string> *res){
	bool draw;
	int startPoz;
	stringstream ss;
	vector<string> tableX, tableO;
	string winner;

	for (int i = 0; i < stoi(com->at(0)); i++) {
		draw = true;
		startPoz = i*5 + 1;
		winner = "NO";

		tableX.push_back(com->at(startPoz));
		tableO.push_back(com->at(startPoz));

		tableX.push_back(com->at(startPoz + 1));
		tableO.push_back(com->at(startPoz + 1));

		tableX.push_back(com->at(startPoz + 2));
		tableO.push_back(com->at(startPoz + 2));

		tableX.push_back(com->at(startPoz + 3));
		tableO.push_back(com->at(startPoz + 3));

		for (int i = 0; i < 4; ++i) {
			ss<<tableX.at(0).at(i)<<tableX.at(1).at(i)<<tableX.at(2).at(i)<<tableX.at(3).at(i);
			tableX.push_back(ss.str());
			tableO.push_back(ss.str());

			ss.str( std::string() );
			ss.clear();
		}

		ss<<tableX.at(0).at(0)<<tableX.at(1).at(1)<<tableX.at(2).at(2)<<tableX.at(3).at(3);
		tableX.push_back(ss.str());
		tableO.push_back(ss.str());
		ss.str( std::string() );
		ss.clear();

		ss<<tableX.at(0).at(3)<<tableX.at(1).at(2)<<tableX.at(2).at(1)<<tableX.at(3).at(0);
		tableX.push_back(ss.str());
		tableO.push_back(ss.str());
		ss.str( std::string() );
		ss.clear();

		//Create table for X and O
		for (unsigned i = 0; i < tableX.size(); i++) {
			replace(tableX.at(i).begin(), tableX.at(i).end(), 'T', 'X');
			replace(tableO.at(i).begin(), tableO.at(i).end(), 'T', 'O');
		}

		for (unsigned i = 0; i < tableX.size(); i++) {
			if ((long) tableX.at(i).find('.') != -1){
				draw = false;
			} else{
				if (tableX.at(i).compare("XXXX") == 0) {
					winner = "X won";
					break;
				}

				if (tableO.at(i).compare("OOOO") == 0) {
					winner = "O won";
					break;
				}
			}
		}

		if (winner.compare("NO") == 0) {
			if (draw) {
				res->push_back("Draw");
			} else {
				res->push_back("Game has not completed");
			}
		} else{
			res->push_back(winner);
		}

		tableX.clear();
		tableO.clear();
	}
}

int main(int argc,char *argv[]) {
	if (argc != 3) {
		cout<<"Problem with parameters"<<endl;
		exit(-1);
	}

	vector<string> com;
	vector<string> res;

	string inputFile = argv[1];
	string outputFile = argv[2];

	inputfileReader(&com, &inputFile);
	Problem_A_Tic_Tac_Toe_Tomek(&com, &res);
	outputfileWriter(&res, &outputFile);

	return 0;
}
