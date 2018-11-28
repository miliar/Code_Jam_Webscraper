#include <iostream>
#include <fstream>
using namespace std;

void search_digits (int digit[10], long long int n) {
	while (n > 0) {
		digit[n%10] = 1;
		n /= 10;
	}
}

int value (int digit[10]) {
	int result = 1;
	int j;
	
	for (j = 0; j < 10; j++) {
		result = result && digit[j];	
	}
	
	return result;
}

int main (int argc, char **argv) {
	ifstream in ("input.txt");
	ofstream out ("output.txt");
	int n_cases, c;
	
	in >> n_cases;
	
	for (c = 1; c <= n_cases; c++) {
		long long int n;
		long long int counter;
		
		in >> n;
		
		if (n == 0) {
			out << "Case #" << c << ":  INSOMNIA" << endl;
		} else {
			int digits[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
			counter = 0;
			
			do {
				counter += n;
				search_digits (digits, counter);
			} while (!value(digits));
			out << "Case #" << c << ":  " << counter << endl;
		}
	}
	
	
	return 0;	
}


