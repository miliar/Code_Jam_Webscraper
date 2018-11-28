#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

int answer;

bool palindromeroot(int number) {
	if (number == 1 || number == 4 || number == 9)
		return true;
	else if (number/10 == number%10)
		return true;
	return false;
}

bool palindrome(int number) {
	if (number < 10) {
		if (number == 1 || number == 4 || number == 9)	
			return true;
	} else if (number > 99 || number < 1000) {
		if (number/100 == number%10) {
			int temp = (int)sqrt(number); //do square
			if (temp * temp == number) {
				if (palindromeroot(temp))
					return true;
			}
		}
	}
	return false;
}

int main() {
	int T, A, B;
	int counter = 1;
	cin >> T;
	while (T-- > 0) {
		answer = 0;
		cin >> A >> B;
		for (int i = A; i <= B; i++)
		{
			if ( i < 10 || i > 100)
			{
				if (palindrome(i))
					answer++;
			}
		}
		cout << "Case #" << counter << ": " << answer << endl;
		counter++;
	}
	return 0;
}