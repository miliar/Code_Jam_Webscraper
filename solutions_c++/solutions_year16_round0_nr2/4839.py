#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <string>

using namespace std;
int optimal(string& input);
void flip(string& input, int bottom);

int main(){
	string input;
	int testNum;
	int optimal_sol;


	getline(cin, input);
	testNum = atoi(input.c_str());

	for(int i = 0; i < testNum; i++){
		getline(cin, input);
		optimal_sol = optimal(input);
		cout << "Case #" << i+1 << ": " << optimal_sol << endl;
	}
	return 0;
}

int optimal(string& input){
	unsigned int pos_count = 0;
	int flip_count = 0;
	unsigned int i = 0;
	char first;

	while(pos_count < input.length()){
		first = input[0];

		if(input[i] == '+'){
			pos_count++;
		}

		if(input[i] != first || i == input.length()){
			flip(input, i-1);
			flip_count++;

			pos_count = 0;
			i = 0;
		}
		else{
			i++;
		}

	}
	return flip_count;
}

void flip(string& input, int bottom){
	int top = 0;

	char top_tmp;
	char bottom_tmp;

	while(top <= bottom){
		if(input[top] == '+'){
			top_tmp = '-';
		}
		else{
			top_tmp = '+';
		}

		if(input[bottom] == '+'){
			bottom_tmp = '-';
		}
		else{
			bottom_tmp = '+';
		}

		input[top] = bottom_tmp;
		input[bottom] = top_tmp;

		top++;
		bottom--;
	}
}