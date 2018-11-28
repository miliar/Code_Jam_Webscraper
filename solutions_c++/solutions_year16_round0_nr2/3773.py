#include <iostream>
#include <string>
using namespace std;
int findPlusMinus(string input);
int findMinusPlus(string input);

string generate(int number);
string generateMinus(int number);
string flip(string input, int number);
int solution(string input);
int main(){
	int number;
	cin >> number;
	string input;
	for (int i = 0; i < number; i++){
		input = "";
		cin >> input;
		cout <<"Case #"<<i+1<<": "<< solution(input) << endl;
	}
}

int solution(string input){
	int counter = 0;
	while (input != generate(input.length())){
		if (input == generateMinus(input.length())){
			return (counter + 1);
		}
		else if (findPlusMinus(input) < findMinusPlus(input)){
			input = flip(input, findPlusMinus(input));
		}
		else{
			input = flip(input, findMinusPlus(input));
		}
		counter++;
	}
	return counter;
}

int findPlusMinus(string input){
	for (int i = 0; i < input.length()-1; i++){
		if ((input[i]=='+') && (input[i + 1] == '-')){
			return i;
		}
	}
	return input.length();
}
int findMinusPlus(string input){
	for (int i = 0; i < input.length() - 1; i++){
		if ((input[i] == '-') && (input[i + 1] == '+')){
			return i;
		}
	}
	return input.length();
}

string generate(int number){
	string output = "";
	for (int i = 0; i < number; i++){
		output += '+';
	}
	return output;
}
string generateMinus(int number){
	string output = "";
	for (int i = 0; i < number; i++){
		output += '-';
	}
	return output;
}
string flip(string input, int number){
	if (input.length() < number){
		cerr << "error" << endl;
	}
	string output = input;
	for (int i = 0; i < number + 1; i++){
		if (input[i] == '+'){
			output[number - i] = '-';
		}
		else{
			output[number - i] = '+';
		}
	}
	return output;
}