#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include <stdlib.h> 

using namespace std;


bool is_find( vector<int>a ){

	for (int i = 0; i < a.size(); i++) {
		if(a[i] == 0) {
			return false;
		}
	}

	return true;
}


int find_one (int input){
	int result = 0;
	
	if (input == 0) {
		return 0;
	}

	vector<int> a(10,0);

	for ( int i = 1; i < 100000000; i++) {
		result = input * i;

		while (result > 0) {
			int tmp = result % 10;
			result /= 10;
			if (a[tmp] == 0) {
				a[tmp] = 1;
			}			
		}

		if ( is_find(a) ) {
				return input * i;
		}

	}



	return result;
}



int main() {

	int count = 1;
	

	ifstream in ("C:/Users/Liao/Desktop/1/A-small-attempt1.in");
	
	if ( !in.is_open() ) {
		cout << "Can not open the input file!" << endl;
	}
	
	
	
	ofstream out ("C:/Users/Liao/Desktop/1/result.txt");

	if ( !out.is_open() ) {
		cout << "Can not open the output file!" << endl;
	}


	string tmp;

	getline(in, tmp);

	int lines_num = atoi ( tmp.c_str() );

	

	while (count <= lines_num ){

		getline(in, tmp);

		int input_data;
		int result;
		
		input_data = atoi ( tmp.c_str() );

		result =  find_one (input_data);

		
		if (result > 0) {
			out << "Case #" << count << ": " << result << endl; 
		}
		else {
			out << "Case #" << count << ": " << "INSOMNIA" << endl; 
		}
		count++;
	

	}


	in.close();
	out.close();

}


















