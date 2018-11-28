// gcjA.cpp
#include <iostream>
#include <fstream>
#include <vector>
//#include <string>
//#include <sstream>


using namespace std;
int get_digit(int input, int digit);

int main()
{
	ifstream infile("input.in");

	ofstream OF("Output.txt");
	int T;
	infile >> T;

	string buf;
	
	
	for (int i = 0; i < T; i++) {

		int N;
		infile >> N;
		vector<int> Digits(10,0);

		int im = 1;

		if (!N) {
			OF << "case #" << i + 1 << ": " <<"INSOMNIA"<< endl;
		}
		else {
			while (find(Digits.begin(), Digits.end(), 0) != Digits.end()) {
				
				for (int id = 0; id < int(1+log10(im*N)); id++) {
					++Digits[get_digit(im*N, id + 1)];
				}
				im++;
				if (im == INT_MAX - 1) {
					cerr << "warning!";
				}
			}
			OF << "case #" << i + 1 << ": " << (im-1)*N << endl;
		}
	
	}

    return 0;
}



int get_digit(int input, int digit) { 
	int A = input / (pow(10, digit));
	int B = input / (pow(10, digit-1));
	return B - 10 * A;

}

