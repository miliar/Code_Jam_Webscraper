//Randall Suliga Jr
//April 10th 2015
//Google Code Jam Submission One, Standing Ovation.

#include<iostream>
#include<fstream>
#include<stdlib.h>

int main(){


std::ifstream input;
std::ofstream output;
char read;
std::string readln;
int num_tests;
int s_max;
int current_s_value;
int people_at_s;
int num_present;
int num_friends;

input.open("A-large.in");
output.open("output.txt");

input >> readln;
num_tests = atoi(readln.c_str());
//std::cout<<num_tests<<std::endl;

for (int case_num = 1; case_num <= num_tests; case_num++){
	num_present = 0;
	num_friends = 0;
	input>>readln;
	//std::cout<<"The read character is: "<<read<<std::endl;
	s_max = atoi(readln.c_str());
	//std::cout<<s_max<<std::endl;
	for (current_s_value = 0; current_s_value<= s_max; current_s_value++){
		while(num_present<current_s_value){
			num_friends++;
			num_present++;
		}
		input>>read;
		people_at_s = read - '0';
		num_present += people_at_s;
	}
	//std::cout<<num_friends<<std::endl;
	output<<"Case #"<<case_num<<": "<<num_friends<<std::endl;
}
input.close();
output.close();

return 0;
}
