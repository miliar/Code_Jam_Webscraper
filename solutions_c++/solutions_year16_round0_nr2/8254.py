#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void flip(bool * pancake, int left) {
	int right = 0;
	while (right <= left) {
		bool temp = pancake[right];
		pancake[right] = !pancake[left];
		pancake[left] = !temp;
		++right;
		--left;
	}
}

int flipPancake(bool * pancake, int size, int times) {
	bool flag = true;
	for (int i = 0; i < size; ++i) {
		flag = flag && pancake[i];
	}
	if (flag) {
		return times;
	}
	if (pancake[0]) {
		int j;
		for (j = 0; pancake[j]; ++j) {}
		flip(pancake, j - 1);
		return flipPancake(pancake, size, times + 1);
	}
	else {
		int j;
		for (j = size - 1; pancake[j]; --j) {}
		flip(pancake, j);
		return flipPancake(pancake, size, times + 1);
	}
}

int main(){
	int T;
	ifstream cin("B-large.in");
	ofstream cout("B-large.out");
	cin >> T;
	for (int i = 0; i < T; ++i) {
		string input;
		cin >> input;
		int size = input.length();
		bool * pancake = new bool[size];
		for (int j = 0; j < size; j++) {
			if (input[j] == '+') {
				pancake[j] = true;
			}
			else {
				pancake[j] = false;
			}
		}
		cout << "Case #" << i + 1 << ": " << flipPancake(pancake, size, 0) << endl;
	}
	return 0;
}