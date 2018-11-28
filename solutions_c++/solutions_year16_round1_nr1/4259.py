#include <iostream>
#include <string>
#include <vector>

using namespace std;


int main(int argc, char* argv[]) 
{
	int cases, len;
	string input, read;
	
	//std::vector<char> read;
	cin >> cases;

	for(int i=1; i<=cases; i++) {
		cin >> input;
		len = input.length();

			read = input[0];
		
			for(int j=1; j<len; j++) {
				if(input[j] < read[0]) {
					read = read + input[j];	
				} else {
					read = input[j] + read ;
				}
			}
			cout << "Case #" << i << ": " << read << "\n";
	}
}