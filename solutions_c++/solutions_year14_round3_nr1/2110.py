/*
 * Qest2.cpp
 *
 *  Created on: Apr 26, 2014
 *      Author: Vibhuti
 */


#include <iostream>
#include <vector>
#include <iterator>
#include <fstream>
#include <sstream>

using namespace std;
int const max_input = 100;
int const min_input = 1;


template <class T>
void stringToInt(string& line,vector<T>& vec){
	istringstream is (line);
	istream_iterator<T> begin(is);
	istream_iterator<T> end;
	vector<T> v( begin,end );
	typename vector<T>::iterator it;
	for(it = v.begin();it!=v.end();it++)
		vec.push_back(*it);
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
		cout << "Number of inputs = " << num_of_input << "\n";

		if(num_of_input > max_input || num_of_input < min_input){
			cout << "Wrong Input FILE\n";
			myfile.close();
			outfile.close();
			return 1;
		}

		for (int i = 1; i <= num_of_input; i++){
			getline(myfile,line);
			stringstream ss;
			ss << line;
			char extra;
			int P, Q;
			ss >> P >> extra >> Q;
			bool imposible =false;

			int myval = 2;
			for (int j = 0; j < 39; j++){
				if (Q == myval || Q ==  (myval * 2)){
					break;
				}
				if(Q > myval && Q < (myval * 2)){
					outfile << "Case #" << i << ": impossible\n";
					imposible = true;
					break;
				}
				myval = myval * 2;
			}
			if (imposible){
				continue;
			}

			float temp = .5, val = (float)P/ (float)Q;
			float result = 0;
			int gen = 0;


			do {
				result = val - temp;
				temp = temp *.5;
				gen++;
			}while (result < 0);
			outfile << "Case #" << i << ": " << gen <<"\n";
		}

	} else
		cout << "Unable to open file";

	myfile.close();
	outfile.close();
	return 0;
}




