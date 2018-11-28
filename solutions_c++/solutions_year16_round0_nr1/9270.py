#include <iostream>
#include <string>
#include <fstream>
#include <set>

void addDigits(int number, std::set<int> &digits){
	while(number > 0){
		int digit = number % 10;
		number = number / 10;
		digits.insert(digit);
	}
}

int main(){
	std::ifstream in("A-small.in");
	std::ofstream out("A-small.out");
	int N;
	in>>N;

	for(int i = 0; i < N; i++){
		int n;
		in>>n;
		std::string output = "Case #" + (std::to_string(i + 1)) + ": ";
		if(n == 0){
			output = output + "INSOMNIA\n";
			out<<output;
			continue;
		}

		std::set<int> digits;
		int bu = 0;
		while(digits.size() < 10){
			bu += n;
			addDigits(bu, digits);
		}

		output = output + (std::to_string(bu)) + '\n';
		out<<output;
	}
	out.close();
	return 0;
}
