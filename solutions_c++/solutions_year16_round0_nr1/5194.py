#include<iostream>
#include<fstream>
using namespace std;

bool *tenDigits=nullptr;

void initializeTenDigits() {
	if (tenDigits == nullptr) {
		tenDigits = new bool[10];

		for (int i = 0;i < 10;i++)
			tenDigits[i] = false;
	}
	else {
		delete tenDigits;
		tenDigits = new bool[10];

		for (int i = 0;i < 10;i++)
			tenDigits[i] = false;
	}
}

void countDigits(int N) {
	
	while (N != 0) {
		tenDigits[N % 10]=true;
		N = N / 10;
	}
}

bool allDigitsFound() {

	for (int i = 0;i < 10;i++)
		if (tenDigits[i] == false)
			return false;

	return true;
}

int main() {

	int T, N,temp;
	//ifstream fin("input.txt");

	ifstream fin("input2.in");
	ofstream fout("output.txt");

	fin >> T;

	for (int i = 0;i < T;i++) {
		fin >> N;
				
		if (N == 0) {
			cout << "Case #" << i + 1 << ": INSOMNIA"<< endl;
			fout << "Case #" << i + 1 << ": INSOMNIA" << endl;
		}
		else {
			initializeTenDigits();

			for (int j = 1;!allDigitsFound();j++) {
				temp = j*N;
				countDigits(temp);
			}
			
			cout << "Case #" << i + 1 << ": " << temp << endl;
			fout << "Case #" << i + 1 << ": " << temp << endl;
		}
	}

	system("pause");
	return 0;
}