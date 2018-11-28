#include <string>
#include <iostream>
#include <fstream>

using namespace std;

// bounded at n flips
void getminflips(string str){

	char current = '+';
	int flips = 0;

	// Look bottom to top
	for(int i = str.length() - 1; i >= 0; i--){
		char c = str[i];

		if(c == current)
			continue;
		else{
			current = c;
			flips++;
		}

	}

	cout << flips;
}


int main(int argc, char *argv[]){

	ifstream file(argv[1]);

	int n;
	file >> n;

	for(int i = 0; i < n; i++){

		string stack;
		file >> stack;

		cout << "Case #" << (i+1) << ": ";
		getminflips(stack);
		cout << endl;
	}
}
