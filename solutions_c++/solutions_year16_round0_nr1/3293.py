#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int count_sheep(int x) {
	int a[10] = { 0 };
	int count = 0;
	int y = x;
	while (x) {
		int temp = x;
		while (temp) {
			int digit = temp % 10;
			if (!a[digit]) {
				a[digit]++;
				count++;
			}
			temp /= 10;
		}
		if (count == 10) {
			return x;
		}
		x += y;
	}
	return 0;
}

int main() {
	ifstream input("A-large.in");
	ofstream output("counting_sheep.txt");
	string num;
	getline(input, num);
	int n = stoi(num);
	for (int i = 0; i < n; ++i) {
		output << "case #" << i + 1 << ": ";
		getline(input, num);
		int number = stoi(num);
		int res = count_sheep(number);
		if (res == 0) output << "INSOMNIA" << endl;
		else output << res << endl;
	}
	return 0;
}