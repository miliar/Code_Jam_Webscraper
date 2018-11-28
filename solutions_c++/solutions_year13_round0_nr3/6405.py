/*
 * fair_square.cpp
 * 
 * Copyright 2013 Antonio <antonio@antonio-laptop>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 */

#include <iostream>
#include <math.h>
#include <fstream>
#include <string.h>
#include <cstdlib>
#include <vector>


using namespace std;


bool is_palyndrome (int parse_number) {
	//How many digits does the number has
	int num_digits = 0;
	int parsed_number = parse_number;
	vector<int> digits;
	while(parsed_number > 0) {
		digits.push_back(parsed_number % 10); 
		parsed_number /=10;
		num_digits++;
	}
	//Rewrite the number as a string of chars
	char number_char[num_digits];
	for(int i = num_digits-1; i>=0 ; i--) {
		number_char[i] = digits.back();
		digits.pop_back();
	}
	//Verify if it is a palyndrome
	int compare_cycles = num_digits/2;
	for(int i = 0; i<compare_cycles;i++) {
		if(number_char[i] != number_char[i+num_digits-1]) {
			return false;
		}
	}
	return true;
}

//Logic
int main(int argc, char** argv)
{
	//Number of test cases
	char cycles_char[4];
	int cycles = 0;
	
	//memset(line, '0',sizeof(line));
	

	//Start to execute the sequence
	string filename = argv[1];
	//Open the filename
	ifstream file_inst (filename.c_str());
	ofstream file_output;
	file_output.open("fair_square.out",ios::out);
	file_inst >> cycles_char;
	//cycles = cycles_char - '0';
	cout<<"The value of cycles char is "<<cycles_char<<endl;
	cycles = atoi(cycles_char);
	cout<<"The value of cycles is "<<cycles<<endl;
	for(int i = 0 ; i < cycles ; i++)//Number of test cases
	{
		//Get the range of numbers	
		int low_limit = 0;
		file_inst >> low_limit;
		cout<<"Value of low limit is "<<low_limit<<endl;
		int high_limit = 0;
		file_inst >> high_limit;
		cout<<"Value of high limit is "<<high_limit<<endl;
		vector <int> chosen;
		for (int p = low_limit; p<= high_limit; p++) {
			bool is_num_palyn = is_palyndrome(p);
			//cout<<"Is playndrome returned "<<is_num_palyn<<endl;
			bool is_sqrt_palyn = false;
			if(is_num_palyn == true) {
				float square_root = sqrt((float)p);
				if((int)square_root*(int)square_root == p)
				{
					is_sqrt_palyn = is_palyndrome(int(square_root));
				}	
			}
			if(is_num_palyn == true && is_sqrt_palyn == true) {
				chosen.push_back(p);
			}
		}
		int temporal = chosen.size();
		cout<<"Chosen value is "<<temporal<<endl;	
		chosen.resize(0);

	
		file_output<<"Case #"<<(i+1)<<": "<<temporal << endl;
	//switch (result) {
	//	case 1 : file_output<<"Case #"<<(i+1)<<": "<<X_won << endl; 
	//		break;
	//	case 2 : file_output<<"Case #"<<(i+1)<<": "<<O_won << endl;
	//		break;
	//	case 3 : file_output<<"Case #"<<(i+1)<<": "<<not_end << endl;
	//		break;
	//	case 4 : file_output<<"Case #"<<(i+1)<<": "<<draw << endl;
	//		break;
	//	}
		
				
	}
	
	file_inst.close();
	file_output.close();
	return 0;
}

