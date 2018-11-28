#include <iostream>
#include <string>
#include <vector>
#include <stdlib.h>
#include <fstream>
using namespace std;
#define MAX 10000
int num[MAX] = {0};
int getcount(char audiences[], int size) {
	num[0] = audiences[0] - 48;
	for(int i = 1; i < size; i++) {
		num[i] = (audiences[i]-48) + num[i-1];
	}

	int max1 = 0;
	for(int i = 1; i < size; i++) {
		max1 = max(max1, i - num[i-1]);
	}
	return max;
}


int main() {
	ifstream myfile;
	int c;
	cin >> c;
	int n = c;
	while(c > 0) {
		int shyness;
		cin >> shyness;
		char audiences[MAX];
		cin >> audiences;

		cout << "Case #" << n - c + 1 << ": " << getcount(audiences, shyness + 1) << endl;
		c--;
	}
	return 0;
}
