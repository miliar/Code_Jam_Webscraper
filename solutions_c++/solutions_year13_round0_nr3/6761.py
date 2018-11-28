#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <iterator>
#include <sstream>
#include <ctype.h>
#include <cmath>

using namespace std;

void split(const string& str, vector<int>& s) {
  stringstream ss(str);
  ss >> noskipws;
  string field;
  int int_field;
  char ws_delim;
  while(1) {
  	if( ss >> field ){
  		int_field = atoi(field.c_str());
  		s.push_back(int_field);
  	} else if (ss.eof()){
  		break;
  	}
    ss.clear();
    ss >> ws_delim;
  }
}
int reverseint(int num_){
        int inv; inv = 0;

        while (num_>0)
        {
                inv = inv * 10 + (num_%10);
                num_ = num_ / 10;
        }

        return inv;
}
int main(){
	fstream input, output;
	string line, number_of_cases;
	int i, int_number_of_cases, x, y;
	char *play_array;
	input.open("input4.in");
	output.open("output4.out");
	if(input.is_open() && output.is_open()){
		getline(input, number_of_cases);
		stringstream ss(number_of_cases);
		if( (ss >> int_number_of_cases).fail() ) {
		  	cout << "error1";
		}
		for(i = 1; i <= int_number_of_cases; i++){
			y = 0;
			vector<int> c;
			
			getline(input, line);
			split(line, c);
			output << "Case #" << i << ": ";
			for(x = c[0]; x <= c[1]; x++){
				if(x == reverseint(x)){
					if(sqrt(x) == reverseint(sqrt(x))){
						y++;
					}
				}
			}
			output << y;
			output << endl;
		}
	} else {
		cout << "Unable to open file";
	}
	
	return 0;
}
