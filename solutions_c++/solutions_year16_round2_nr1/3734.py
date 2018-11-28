#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<string> numbers;
vector<string> digitsString;

string search(int curr, int* count) {
	bool emptyCount = true;
	for(int i = 0; i < 26; i++) {
		if(count[i] != 0) {
			emptyCount = false;
			break;
		}
	}

	if(emptyCount) {
		return "";
	}

	if(curr > 9) {
		return "#";
	}

	string str = numbers[curr];
	int* digits = new int[26];
	for(int i = 0; i < 26; i++) {
		digits[i] = 0;
	}
	for(int i = 0; i < str.length(); i++) {
		digits[str[i] - 'A']++;
	}
	bool found = true;
	for(int i = 0; i < 26; i++) {
		if(digits[i] > count[i]) {
			found = false;
			break;
		}
	}

	if(found) {
		for(int i = 0; i < str.length(); i++) {
			count[str[i] - 'A']--;
		}
		string res = search(curr, count);
		if(res != "#") {
			return digitsString[curr] + res;
		}
		else {
			for(int i = 0; i < str.length(); i++) {
				count[str[i] - 'A']++;
			}
			return search(curr + 1, count);
		}
	}
	else {
		return search(curr + 1, count);
	}
}

int main() {
	int t;
	cin >> t;
	digitsString.push_back("0");
    digitsString.push_back("1");
    digitsString.push_back("2");
    digitsString.push_back("3");
    digitsString.push_back("4");
    digitsString.push_back("5");
    digitsString.push_back("6");
    digitsString.push_back("7");
    digitsString.push_back("8");
    digitsString.push_back("9");

    numbers.push_back("ZERO");
    numbers.push_back("ONE");
    numbers.push_back("TWO");
    numbers.push_back("THREE");
    numbers.push_back("FOUR");
    numbers.push_back("FIVE");
    numbers.push_back("SIX");
    numbers.push_back("SEVEN");
    numbers.push_back("EIGHT");
    numbers.push_back("NINE");
	for(int j = 1; j <= t; j++) {
		cout << "Case #" << j << ": ";
		string str;
		cin >> str;

		int* count = new int[26];
		for(int i = 0; i < 26; i++) {
			count[i] = 0;
		}
		for(int i = 0; i < str.length(); i++) {
			count[str[i] - 'A']++;
		}

		cout << search(0, count) << endl;
	} 
	return 0;
}