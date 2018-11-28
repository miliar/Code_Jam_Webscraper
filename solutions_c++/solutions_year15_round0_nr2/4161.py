//Randall Suliga Jr
//April 10th 2015
//Google Code Jam Submission Two, Pancakes

#include<iostream>
#include<fstream>
#include<stdlib.h>
#include <sstream>
#include<string>

int limit(int current_limit, int num_test, int how_many){
	if(num_test == 1){
		return 1;
	}
	if(num_test == 1){
		return 2;
	}
	if ( current_limit >= num_test){
		return current_limit;
	}

	int time=0;
	int min_time=num_test+1;
	int min_limit = current_limit;
	int num_test_copy = num_test;
	while(current_limit <= num_test){
		time = 0;
		while (num_test_copy > current_limit){
			time+=how_many;
			num_test_copy-=current_limit;
		}
		time+=current_limit;
	/*	if (time == min_time){
			min_time = time;
			if(current_limit != num_test){
				min_limit = current_limit;
			}
		}*/
		if (time <= min_time){
			min_time = time;
			min_limit = current_limit;
		}
		current_limit++;
		num_test_copy = num_test;
	}
	return min_limit;
}

int main(){


std::ifstream input;
std::ofstream output;
char read;
std::string readln;
int num_tests;
int num_diners;
int pancakes[1001];
int tempcakes[1001];
int num_minutes;
int min_minutes;
int num_passed;
int max_pan;
int max_pan2;
int num_pancakes;

input.open("B-small-attempt8.in");
output.open("output4.txt");

input >> readln;
num_tests = atoi(readln.c_str());
//std::cout<<num_tests<<std::endl;

for (int case_num = 1; case_num <= num_tests; case_num++){

	//std::cout<<"We are on case "<<case_num<<std::endl;
	for (int i = 0; i<=1000; i++){
		pancakes[i] = 0;
	}

	max_pan = 0;
	num_minutes = 0;
	input>>readln;
	num_diners = atoi(readln.c_str());
	//std::cout<<num_diners<<" is the number of nonzero diners"<<std::endl;
	//
	//
	for (int diner_num = 1; diner_num <= num_diners; diner_num++){
		input>>readln;
		std::istringstream stream(readln);
		stream >> num_pancakes;
		//std::cout<<"Diner has "<<num_pancakes<<" pancakes"<<std::endl;
	
		if(num_pancakes > max_pan){
			max_pan = num_pancakes;
		}
		pancakes[num_pancakes]++;
		}
		//std::cout<<"Maximum Pancakes: "<<max_pan<<" Round "<<case_num<<std::endl;

	min_minutes = max_pan;

	int cur_limit = 1;

	for (int i = 1 ; i<=max_pan ; i++){
		if (pancakes[i] != 0){
			cur_limit = limit(cur_limit,i,pancakes[i]);
		}
	}

	//std::cout<<"The first number we need to reduce to is: "<<cur_limit<<std::endl;
	
	int other_limit=cur_limit;
	int test_limit=cur_limit;

	while(1){
		for (int i = 1 ; i<=max_pan ; i++){
			if (pancakes[i] != 0){
				other_limit = limit(other_limit,i,pancakes[i]);
			}
		}	
		//std::cout<<"The next number we need to reduce to is: "<<cur_limit<<std::endl;
		if ( other_limit == cur_limit){
			break;
		}
		cur_limit = other_limit;
		
	}

	//std::cout<<"The lowest number we need to reduce to is: "<<cur_limit<<std::endl;

	int checking = cur_limit+1;
	min_minutes = cur_limit;
	int temp_holder;

	while (max_pan >= checking){
		if (pancakes[checking] != 0){
			temp_holder = checking;
			while (temp_holder > cur_limit){
				min_minutes+=pancakes[checking];
				temp_holder-=cur_limit;
			}
		}
		checking++;
	}

	output<<"Case #"<<case_num<<": "<<min_minutes<<std::endl;
}

/*

	std::cout<<limit(1,4,1)<<std::endl;
	std::cout<<limit(2,4,1)<<std::endl;
	std::cout<<limit(3,4,1)<<std::endl;	

	std::cout<<limit(1,4,2)<<std::endl;
	std::cout<<limit(2,4,2)<<std::endl;
	std::cout<<limit(3,4,2)<<std::endl;	

	std::cout<<limit(1,4,3)<<std::endl;
	std::cout<<limit(2,4,3)<<std::endl;
	std::cout<<limit(3,4,3)<<std::endl;	

	*/

input.close();
output.close();

return 0;
}
