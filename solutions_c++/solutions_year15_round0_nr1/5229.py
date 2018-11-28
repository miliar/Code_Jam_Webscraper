#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests(0);
	
	cin >> tests;

	for (int test = 1; test <= tests; ++test) {
		int smax(0);
		string str;
		cin >> smax >> str;

		int standing(0), my_friends(0);
		for (int i = 0; i < str.length(); ++i) {
			if (standing >= i) {
				standing += str[i] - '0';
			}
			else if (str[i] - '0' != 0) {
				int dif = i - standing;
				standing += dif + str[i] - '0';
				my_friends += dif;
			}
		}

		cout << "Case #" << test << ": " << my_friends << endl;
	}
	return 0;
}