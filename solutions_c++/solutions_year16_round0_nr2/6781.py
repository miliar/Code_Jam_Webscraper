#include<fstream>
#include<iostream>

using namespace std;

int strlen(char* arr) {
	int len = 0;
	for (len = 0;; len++) {
		if (arr[len] == '\0') {
			break;
		}
	}
	return len;
}

void strtobool(char* arr, bool* to, int size) {
	for (int i = 0; i < size; i++) {
		if (arr[i] == '+') {
			to[i] = true;
		}
		else {
			to[i] = false;
		}
	}
}

void flip(bool* arr, int n) {
	for (int i = 0; i <=n ; i++) {
		arr[i] = !arr[i];
	}
}

int waitor(bool* pan, int size) {
	int cnt = 0;
	for (int i = 1; i < size; i++) {
		if (pan[i] != pan[i - 1]) {
			flip(pan, i-1);
			cnt++;
		}
	}
	if (pan[0] == false) {
		cnt++;
	}
	return cnt;
}

int main(void) {
	ofstream outFile("output.out");
	ifstream inFile("input.in");
	int T;
	inFile >> T;										//get T
	int* result = new int[T];
	char** pancake = new char*[T];
	for (int i = 0; i < T; i++) {
		pancake[i] = new char[101];
		inFile >> pancake[i];
		int size = strlen(pancake[i]);
		bool* pan = new bool[size];
		strtobool(pancake[i], pan, size);
		result[i] = waitor(pan, size);
	}
	for (int i = 0; i < T; i++) {
		if (result[i] == -1) {
			outFile << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
		}
		else {
			outFile << "Case #" << i + 1 << ": " << result[i] << endl;
		}
	}
	return 0;
}