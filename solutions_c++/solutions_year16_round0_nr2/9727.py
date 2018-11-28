#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

int count_moves (char *pan) {
	int i;
	int counter = 0;
	int tmp = pan[0];
	for (i = 1; i < strlen(pan); i++) {
		if (pan[i] != tmp) {
			counter++;
			tmp = pan[i];
		}
	}
	
	if (tmp == '-')
		counter++;
		
		return counter;	
}

int main (int argc, char **argv) {
	ifstream in ("input.txt");
	ofstream out ("output.txt");
	int n_cases, c;
	int i = 0;
	int n_moves;
	
	in >> n_cases;
	
	for (c = 1; c <= n_cases; c++) {
		char array[101];
		
		in >> array;
		
		n_moves = count_moves (array);
		out << "Case #" << c << ":  " << n_moves << endl;
	}
	
	
	return 0;	
}



