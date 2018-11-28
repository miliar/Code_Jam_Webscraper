#include <iostream>
#include <unordered_set>
using namespace std;

int main(){
	int cases, numberCase, multiplier, length;
	string stringCase;
	unordered_set<char> digits(10);
	cin >> cases;
	++cases;
	for(int c = 1; c < cases; ++c){
		digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
		cin >> numberCase;
		stringCase = to_string(numberCase);
		if(numberCase == 0){
			cout << "Case #" << c << ": INSOMNIA\n";
			continue;
		}
		multiplier = 1;
		while(digits.size() > 0){
			stringCase = to_string(numberCase*multiplier++);
			length = stringCase.length();
			for(int i = 0; i < length; ++i){
				digits.erase(stringCase.at(i));
			}
		}
		cout << "Case #" << c << ": " << stringCase << '\n';
	}
}