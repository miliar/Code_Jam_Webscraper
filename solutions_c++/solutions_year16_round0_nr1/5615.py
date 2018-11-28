#include <iostream>
#include <fstream>

using namespace std;

void markNumbers(int n, bool* arr) {
	while(n > 0) {
		int num = n % 10;
		arr[num] = true;
		n /= 10;
	}
}

bool allNumbersSeen(bool* arr) {
	for(int i = 0; i < 10; ++i) {
		if(arr[i] == false) {
			return false;
		}
	}
	return true;
}

void markAllFalse(bool* arr) {
	for(int i = 0; i < 10; ++i) {
		arr[i] = false;
	}
}

int main(int argc, char* argv[]) {
	if(argc != 2) {
		cout << "Usage: use this program correctly" << endl;
		return 0;
	}
	ofstream os("out.txt");
	ifstream is(argv[1]);
	int numTestCases;
	is >> numTestCases;
	for(int i = 1; i <= numTestCases; ++i) {
		os << "Case #" << i << ": ";
		int n;
		is >> n;

		bool numbersSeen[10];
		markAllFalse(numbersSeen);
		for(int j = 1; j < 4200; ++j) {
			markNumbers(j*n, numbersSeen);
			if(allNumbersSeen(numbersSeen)) {
				os << j*n << endl;
				break;
			}
		}
		if(!allNumbersSeen(numbersSeen)) {
			os << "INSOMNIA" << endl;
		}
	}
}