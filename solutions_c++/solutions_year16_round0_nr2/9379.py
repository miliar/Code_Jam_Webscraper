#include <iostream>
#include <fstream>

int main(){
	std::ifstream in("B.in");
	std::ofstream out("B.out");
	int N;
	std::string input;
	std::getline(in, input);
	N = std::stoi(input);

	for(int i = 0; i < N; i++){
		std::getline(in, input);
		char curChar = input[0];
		int segments = 0;
		for(int j = 0; j < input.size(); j++){
			if(curChar != input[j]){
				segments++;
				curChar = input[j];
			}
		}
		if(input[input.size() - 1] == '-'){
			segments++;
		}
		std::cout<<"Case #"<<(i+1)<<": "<<segments<<'\n';
		out<<"Case #"<<(i+1)<<": "<<segments<<'\n';
	}
	out.close();
	return 0;
}
