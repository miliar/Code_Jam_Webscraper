#include<fstream>
#include<iostream>

using namespace std;

int pow10(int n) {
	int result=1;
	for (int i = 0; i < n; i++) {
		result *= 10;
	}
	return result;
}
int log10(int n) {
	int cnt = 0;
	int pow = 1;
	while (pow<=n) {
		pow *= 10;
		cnt++;
	}
	return cnt;
}
void parse(bool* arr, int n) {
	for (int i = 0; i <log10(n); i++) {
		int temp = (n / pow10(i)) % 10;
		arr[temp] = true;
	}
}
int count(bool* arr,int n) {
	bool stop = 0;
	int cnt = 0;
	while (!stop) {
		stop = 1;
		cnt++;
		parse(arr, cnt*n);
		for (int j = 0; j < 10; j++) {
			stop *= arr[j];
		}
	}
	return n*cnt;
}


int main(void) {
	ofstream outFile("output.out");
	ifstream inFile("input.in");
	int T;
	inFile >> T;										//get T
	int* n = new int[T];
	int* result = new int[T];
	bool** arr = new bool*[T];
	for (int i = 0; i < T; i++) {
		inFile >> n[i];								//get n
		arr[i] = new bool[10];						//determines if i has been seen
		for (int j = 0; j < 10; j++) {
			arr[i][j] = false;
		}
		if (n[i] == 0) {
			result[i] = -1;
		}
		else {
			result[i] = count(arr[i],n[i]);
		}
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