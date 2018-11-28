#include <vector>
#include <sstream>
#include <iostream>
#include <fstream>
using namespace std;

void countDigits(int num, vector<int>& digits) {
	if (num < 10) {
		digits.push_back(num);
		return;
	}
	digits.push_back(num % 10);
	countDigits(num / 10, digits);
}

void checkNum(vector<bool>& nums, int n) {
	vector<int> digits;
	countDigits(n, digits);
	for (int i : digits) {
		nums[i] = true;
	}
}

bool checkIfTrue(const vector<bool>& nums) {
	for (bool i : nums) {
		if (i == false) return false;
	}
	return true;
}

int countSheep(int n) {
	if (n == 0) return n;
	vector<bool> nums;
	for (int i = 0; i < 10; i++) {
		nums.push_back(false);
	}
	int num;
	for (int i = 1; !checkIfTrue(nums); i++) {
		num = i*n;
		checkNum(nums, num);
	}
	return num;
}

int main() {
	string ifName;
	cin >> ifName;
	ofstream of("output.txt");
	ifstream iS(ifName);
	int n;
	int inputs;
	iS >> inputs;
	for (int i = 0; i < inputs; i++) {
		iS >> n;
		int sheep = countSheep(n);
		if (sheep == 0) of << "case #" << i + 1 << ": " << "INSOMNIA" << endl;
		else of << "case #" << i + 1 << ": " << sheep << endl;
	}
}