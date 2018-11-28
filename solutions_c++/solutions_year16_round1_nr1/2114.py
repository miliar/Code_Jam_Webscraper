#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <vector>

using namespace std;  // since cin and cout are both in namespace std, this saves some text
void main() {
	long long int t, n;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		char input[1500];
		cin >> input;  // read n and then m.
		long long int count = 1;
		vector<char> output;
		output.push_back(input[0]);
		char first = input[0];
		char last = input[0];
		while (input[count] != '\0')
		{
			if (input[count] >= first) {
				output.insert(output.begin(), input[count]);
				first = input[count];
				count++;
			}
			else {
				output.push_back(input[count]);
				count++;
			}
		}
			
		cout << "Case #" << i << ": ";
		for (int j = 0; j < output.size(); ++j) {
			cout << output[j];
		}
		cout << endl;
	}
}