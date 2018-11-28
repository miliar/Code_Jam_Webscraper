#include<iostream>
#include<math.h>
using namespace std;
bool squre[1000];
bool palindrome[1000];

void generateSqure() {
	for (int i = 1; i < 31; i++) {
		squre[i * i] = true;
	}
}
bool isPalindrome(int x) {
	int temp = x;
	int sum = 0, r = 0;
	;
	while (temp) {
		r = temp % 10;
		sum = (sum * 10) + r;
		temp = temp / 10;
	}
	if (x == sum)
		return true;

	return false;
}
void generatePalindrome() {
	for (int i = 1; i < 1000; i++) {
		palindrome[i] = isPalindrome(i);
	}
}
int solve(int start, int end) {
	int count = 0;
	for (int i = start; i <= end; i++) {
		if (palindrome[i]) {
			if (squre[i]) {
				if (palindrome[(int) sqrt(i)])
					count++;
			}
		}
	}
	return count;

}

int main() {

	generateSqure();
	generatePalindrome();

	int noOfTestCases = 0;
	int start = 0, end = 0;
	cin >> noOfTestCases;
	for (int i = 1; i < noOfTestCases + 1; i++) {
		cin >> start;
		cin >> end;
		cout << "Case #" << i << ": " << solve(start, end) << endl;
	}

	return 0;
}
