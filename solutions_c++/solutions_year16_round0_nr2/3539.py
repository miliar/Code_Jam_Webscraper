#include <iostream>
#include <fstream>
#include <string>

using namespace std;

string flipAll(string input) {
	for (int i = 0; i < input.length(); ++i)
	{
		if(input[i] == '+') input[i] = '-';
		else input[i] = '+';
	}
	return input;
}

bool checkIfSolved(string input){
	for (int i = 0; i < input.length(); ++i)
	{
		if(input[i] == '-') return false;
	}
	return true;
}

long countFlipsNeeded(string input, long count){
	if(input.length() == 0 || checkIfSolved(input)) return count;

	if(input[input.length() - 1] == '-'){
		input = input.substr(0,input.length()-1);
		input = flipAll(input);
		count++;
		count = countFlipsNeeded(input,count);
	}else if(input[input.length() - 1] == '+'){
		input = input.substr(0,input.length()-1);
		count = countFlipsNeeded(input,count);
	}
	return count;
}




int main(){
	ifstream input("inputs.txt");
	ofstream output("output.txt");
	long numberOfInputs,result,counter = 0;
	input >> numberOfInputs;
	string panCakesOrder;
	while (numberOfInputs > 0) {
		counter++;
		input >> panCakesOrder;
		result = countFlipsNeeded(panCakesOrder,0);
		output << "Case #" << counter << ": " << result << endl; 
		numberOfInputs--;
	}
	input.close();
	output.close();
	return 0;
}