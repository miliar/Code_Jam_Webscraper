//Randall Suliga Jr
//April 11th 2015
//Google Code Jam Submission Two, Pancakes

#include<iostream>
#include<fstream>
#include<stdlib.h>
#include <sstream>
#include<string>

int main(){


std::ifstream input;
std::ofstream output;
char read;
std::string readln;
int X;
int R;
int C;
int num_tests;
int area;
bool pass = false;
std::string answer;
int max_dim;
int min_dim;
int max_side;
int min_side;

input.open("D-small-attempt2.in");
output.open("output2.txt");

input >> readln;
num_tests = atoi(readln.c_str());
//std::cout<<num_tests<<std::endl;

std::stringstream stream;

for (int case_num = 1; case_num <= num_tests; case_num++){

	//std::cout<<"We are on case "<<case_num<<std::endl;

		input>>readln;
		//std::cout<<"The stream is "<<stream<<std::endl;
		//std::cout<< "Readln is "<<readln<<std::endl;
		X = atoi(readln.c_str());

		input>>readln;
		R = atoi(readln.c_str());
			
		input>>readln;
		C = atoi(readln.c_str());
		//std::cout<<"The box is "<<R<<" rows by "<<C<<" Columns."<<std::endl;	
		
		if (R>C){
			max_side = R;
			min_side = C;
		}
		else{
			max_side = C;
			min_side = R;
		}

		area = R * C;
		if(area < X){
			pass=false;
		}
		else{
			area= area%X;
			if (area == 0){
				pass=true;
			}
			else{
				pass=false;
			}
		}

		min_dim = X/2;
		max_dim = X-min_dim;
		if (max_dim == min_dim){
			max_dim +=1;
		}
		else if (max_dim != min_dim){
			min_dim = max_dim;
		}

		if (max_side < max_dim || min_side < min_dim ){
			pass=false;
		}



		if (X == 4 && ( (C<=2) || (R<=2) )){
			pass=false;
		}
		
		if(X>=7){
			pass=false;
		}

		if (pass){
			answer = "GABRIEL";
		}
		else{
			answer = "RICHARD";
		}		

	output<<"Case #"<<case_num<<": "<<answer<<std::endl;
}
input.close();
output.close();

return 0;
}
