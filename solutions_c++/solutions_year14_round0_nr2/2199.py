//============================================================================
// Name        : Cookie_Clicker_Alpha.cpp
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

void stringToFloat(string& line,vector<long double>& vec){

   istringstream is (line);
   istream_iterator<long double> begin(is);
   istream_iterator<long double> end;
   vector<long double> v( begin,end );

   for(vector<long double>::iterator it = v.begin();it!=v.end();it++){
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
			vector<long double> vec_d;
			line.clear();
			getline(myfile,line);
			stringToFloat(line,vec_d);
			long double C, F, X, TimeC = 0, TimeX = 0, Result = 0, Previous_Result = 0;
			C = vec_d[0];
			F = vec_d[1];
			X = vec_d[2];
			for (int j = 0; true; j++){
				 TimeC = C / (2 + j*F);
				 TimeX = X / (2 + j*F);
				 if (Previous_Result != 0 && Previous_Result < Result + TimeX){
					 Result = Previous_Result;
					 break;
				 }
				 Previous_Result = Result + TimeX;
				 Result = Result + TimeC;

			}
			outfile.precision(20);
			outfile << "Case #" << i << ": " << Result << "\n";
		}

	} else
		cout << "Unable to open file";


	return 0;
}
