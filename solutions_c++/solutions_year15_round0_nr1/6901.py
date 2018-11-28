#include<iostream>
#include<string>

using namespace std;

int main() {

	int test = 0;
	cin >> test;
	int a = 1;

	while (a <= test) {

		int maxshyness;
		char digits [1008];
		cin >> maxshyness >> digits;
		long long count = 0;
		long long friends = 0;
		for (int i = 0; i <= maxshyness; ++i) {
			char ch = digits[i];
			if (count >= i) {
				count += atoll(&ch);
				continue;
			} else {
				int diff = i - count;
				friends += diff;
				count += diff;
				count += atoll(&ch);

			}

		}

		cout << "Case #" << a << ": " << friends << endl;

		a++;




	}




	return 0;
}

