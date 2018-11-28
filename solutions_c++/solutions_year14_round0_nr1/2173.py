//============================================================================
// Name        : Magic_Trick.cpp
// Author      : Vibhuti
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <iterator>
#include <fstream>
#include <sstream>

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

		if(num_of_input > 100 || num_of_input < 1){
			cout << "Wrong Input FILE\n";
			myfile.close();
			outfile.close();
			return 1;
		}

		for (int i = 1; i <= num_of_input; i++){
			vec.clear();
			line.clear();
			getline(myfile,line);
			stringToInt(line, vec);
			int ans_first = vec[0];
			vector<int> ans_first_row;
			vector<int> ans_second_row;
			vector<int> selection;

			if(ans_first > 4 || ans_first < 1){
				cout << "Wrong Choice\n";
				myfile.close();
				outfile.close();
				return 2;
			}

			for (int j = 1; j <= 4; j++){
				vec.clear();
				line.clear();
				getline(myfile,line);
				stringToInt(line, vec);
				if(j == ans_first){
					ans_first_row = vec;
				}
			}

			vec.clear();
			line.clear();
			getline(myfile,line);
			stringToInt(line, vec);
			int ans_second = vec[0];
			if(ans_second > 4 || ans_second < 1){
				cout << "Wrong Choice\n";
				myfile.close();
				outfile.close();
				return 3;
			}

			for (int j = 1; j <= 4; j++){
				vec.clear();
				line.clear();
				getline(myfile,line);
				stringToInt(line, vec);
				if(j == ans_second){
					ans_second_row = vec;
				}
			}
			for (int j = 0; j < 4; j++){
				for (int k = 0; k < 4; k++){
					if (ans_first_row[j] == ans_second_row[k])
						selection.push_back(ans_first_row[j]);
				}
			}

			outfile << "Case #" << i << ": ";

			switch (selection.size()){

				case 0:
					outfile << "Volunteer cheated!\n";
					break;
				case 1:
					outfile << selection[0] << "\n";
					break;
				default:
					outfile << "Bad magician!\n";
					break;

			}

		}

	} else
		cout << "Unable to open file";


	return 0;
}
