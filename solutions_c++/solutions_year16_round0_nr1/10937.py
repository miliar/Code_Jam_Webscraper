#include <iostream>
#include <fstream>
using namespace std;
unsigned int pow(unsigned int input);
unsigned int getLength(unsigned int input);
unsigned int getValue(unsigned int input);

int main() {
	unsigned int t;
	ifstream file("A-large.in");
	file >> t;
	unsigned int *p_input = new unsigned int[t];
	for(unsigned int i = 1; i <= t; i++)
		file >> p_input[i];
	file.close();
	ofstream ofile("A-large.out");
	for(unsigned int i = 1; i<= t; i++){
		ofile << "Case #" << i << ": ";
		unsigned int output = getValue(p_input[i]);
		if(output)
			ofile << output << endl;
		else
			ofile << "INSOMNIA" << endl;
	}
	delete [] p_input;
	return 0;
}

unsigned int pow(unsigned int input){
	unsigned int times = 1;
	for(unsigned int i=0; i<input; i++)
		times *= 10;
	return times;
}

unsigned int getLength(unsigned int input){
	unsigned int i = 0;
	while(input/pow(i))
		i++;
	return i;
}

unsigned int getValue(unsigned int input){
	if(!input)
		return 0;
	int digits[10] = {1,1,1,1,1,1,1,1,1,1};
	unsigned int count = 0, n = 1;
	unsigned int number = input;
	while(count<10){
		number = input*n;
		unsigned int length = getLength(number);
		unsigned int *p_number = new unsigned int[length];
		unsigned int temp_number = number;
		for(unsigned int i=0; i<length; i++){
			p_number[i] = temp_number / pow(length - i -1);
			temp_number -= p_number[i]*pow(length - i -1);
		}
		for(unsigned int i = 0; i<length; i++){
			if(digits[p_number[i]]){
				digits[p_number[i]] = 0;
				count++;
			}
		}
		delete [] p_number;
		n++;
	}
	return number;
} 
