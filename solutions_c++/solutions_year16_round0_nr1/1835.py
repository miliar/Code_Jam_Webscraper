#include <iostream>
#include <fstream>

using namespace std;

bool checkNum(int *arr, int temp) {
	while (temp > 0) {
		int t = temp % 10;
		temp /= 10;
		arr[t] |= 1;
	}

	for (int i = 0; i < 10; i++) {
		if (arr[i] == 0)
			return false;
	}

	return true;
}

int main() {
	ifstream in("A-large.in");
	ofstream out("largeoutput.txt");
	int cases, num;
	in >> cases;
	for (num = 1; num <= cases; ++num) {
		int N;
		int arr[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
		in >> N;
		if (N == 0) {
			out << "Case #" << num << ": INSOMNIA" << endl;
			continue;
		}
		
		for (int i = 1;; ++i) {
			int temp = i * N;
			if (checkNum(arr, temp)) {
				out << "Case #" << num << ": " << temp << endl;
				break;
			}
		}
		
	}
 	return 0;
}