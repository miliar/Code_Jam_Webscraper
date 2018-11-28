#include <iostream>
#include <string>
using namespace std;

int main(){
	int cases, sLength;
	string input, output;
	cin >> cases;
	++cases;
	for(int c = 1; c < cases; ++c){
		cin >> input;
		sLength = input.length();
		output = input.at(0);
		for(int i = 1; i < sLength; ++i){
			if(input[i] <= output.back()){
				output.insert(output.end(),input[i]);
			}
			else if(input[i] < output.front()){
				output.insert(output.end(),input[i]);
			}
			else output.insert(output.begin(), input[i]);
		}
		cout << "Case #" << c << ": " << output << '\n';
	}

}