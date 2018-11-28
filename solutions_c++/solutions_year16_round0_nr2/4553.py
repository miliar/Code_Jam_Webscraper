#include <string>
#include <iostream>

using namespace std;

int countFlips(string &input_string) {
	char prev = input_string[0];
	int switches = 0;
	char c;

	for(int j = 0; j < input_string.length(); j++) {
		c = input_string[j];
			
		if(c != prev) {
			switches++;
		}
		
		prev = c;
	}
	if(c == '-') {
		switches++;	
	}

	return switches;
}

int main() {
	string input;
	int T;
	cin >> T;
	for(int i = 0; i < T; i++) {
		//getline(cin, input);
		cin >> input;
		//cout << input << endl;
	  cout <<	"Case #" << i+1 << ": " << countFlips(input) << endl;
	}

}