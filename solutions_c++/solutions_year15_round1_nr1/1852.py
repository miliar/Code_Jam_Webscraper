#include<iostream>
#include<fstream>
#include<stdlib.h>
#include <sstream>
#include<string>

int main(){

	std::string readln;
	std::ifstream input;
	std::ofstream output;
	int num_tests;	
	int num_intervals;
	long long answer_1;
	int max_dif;
	int dif;
	long long answer_2;

	input.open("A-large.in");
	output.open("output.txt");


	input >> readln;
	num_tests = atoi(readln.c_str());

	for (int case_num = 1; case_num <= num_tests; case_num++){

	input >> readln;
	num_intervals = atoi(readln.c_str());
	
	int shrooms[num_intervals];



	for (int i = 0; i < num_intervals; i++){
		input >> readln;
		shrooms[i]= atoi(readln.c_str());
		//std::cout<<shrooms[i]<<" ";
	}

	//std::cout<<std::endl;

	answer_1 = 0;
	max_dif = 0;

	for (int i = 1; i < num_intervals; i++){
		dif = shrooms[i-1]-shrooms[i];
		if (dif > 0){
		answer_1 += dif;
		}
		if (dif > max_dif){
			max_dif = dif;
		}

	}

	answer_2=0;

	for (int i =0; i < num_intervals-1; i++)
	{
		if (shrooms[i]<max_dif){
			answer_2+=shrooms[i];
		}
		else{
		answer_2+=max_dif;
		}	
	}	

		output<<"Case #"<<case_num<<": " <<answer_1<<" "<<answer_2<<std::endl;


	

	}




	input.close();
	output.close();

	return 0;
}
