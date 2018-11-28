//============================================================================
// Name        : Deceitful_War.cpp
// Author      : Vibhuti
// Version     :
// Copyright   : Your copyright notice
// Description : Deceitful War in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <iterator>
#include <fstream>
#include <sstream>
#include <algorithm>

using namespace std;

void stringToInt(string& line,vector<int>& vec){

   istringstream is (line);
   istream_iterator<int> begin(is);
   istream_iterator<int> end;
   vector<int> v( begin,end );

   for(vector<int>::iterator it = v.begin();it!=v.end();it++){
                vec.push_back(*it);
   }

}

void stringToFloat(string& line,vector<double>& vec){

   istringstream is (line);
   istream_iterator<double> begin(is);
   istream_iterator<double> end;
   vector<double> v( begin,end );

   for(vector<double>::iterator it = v.begin();it!=v.end();it++){
                vec.push_back(*it);
   }

}

int main() {
	string line;
	ifstream myfile;
	ofstream outfile;
	myfile.open ("input.txt");
	outfile.open ("output.txt");

	if(myfile.is_open() && outfile.is_open()){
		getline(myfile,line);
		vector<int> vec;
		stringToInt(line, vec);
		int num_of_input = vec[0];
		//cout << "Number of inputs = " << num_of_input << "\n";

		if(num_of_input > 50 || num_of_input < 1){
			cout << "Wrong Input FILE\n";
			myfile.close();
			outfile.close();
			return 1;
		}

		for (int i = 1; i <= num_of_input; i++){
			int blocks, Naomi_win = 0, Naomi_win_d = 0;
			vector<double> Naomi;
			vector<double> Naomi_d;
			vector<double> Ken;
			vector<double> Ken_d;
			vec.clear();
			line.clear();
			getline(myfile,line);
			stringToInt(line,vec);
			blocks = vec[0];

			line.clear();
			getline(myfile,line);
			stringToFloat(line,Naomi);

			line.clear();
			getline(myfile,line);
			stringToFloat(line,Ken);

			std::sort(Naomi.begin(),Naomi.end());
			std::sort(Ken.begin(),Ken.end());
			Naomi_d = Naomi;
			Ken_d = Ken;
// WAR
			for (int j = 0; j < blocks; j++){
				if (Naomi[Naomi.size() - 1] > Ken[Ken.size() - 1]){
					Naomi.erase(Naomi.end() - 1);
					Ken.erase(Ken.begin());
					Naomi_win++;
				} else {
					for (int k = 0; k < Ken.size(); k++){
						if (Naomi[Naomi.size() - 1] < Ken[k]){
							Naomi.erase(Naomi.end() - 1);
							Ken.erase(Ken.begin() + k);
							break;
						}
					}
				}
			}

// DECEITFUL WAR
			for (int j = 0; j < blocks; j++){
				if (Naomi_d[Naomi_d.size() - 1] > Ken_d[Ken_d.size() - 1]){
					for (int k = 0; k < Naomi_d.size(); k++){
						if (Naomi_d[k] > Ken_d[0]){
							Naomi_d.erase(Naomi_d.begin() + k);
							Ken_d.erase(Ken_d.begin());
							Naomi_win_d++;
							break;
						}
					}
				} else {

					Ken_d.erase(Ken_d.end() - 1);
					Naomi_d.erase(Naomi_d.begin());

				}
			}

//			cout << "Case #" << i << ": " << Naomi_win_d << " " << Naomi_win << "\n";
			outfile << "Case #" << i << ": " << Naomi_win_d << " " << Naomi_win << "\n";
		}

	} else
		cout << "Unable to open file";


	return 0;
}
