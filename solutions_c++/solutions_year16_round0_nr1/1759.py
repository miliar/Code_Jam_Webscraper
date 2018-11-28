#include <iostream>
#include <vector>
#include <string>

using namespace std;

void test()
{
	long long n;
	cin >> n;
	vector<bool> hasDigit(10, false);
	for (int i = 1; i <= 10000; i++) {
		long long x = n * i;
		string s = to_string(x);
		for (auto c : s) {
			hasDigit[c - '0'] = true;
		}
		bool finish = true;
		for (int j = 0; j < 10; j++) {
			if (!hasDigit[j]) {
				finish = false;
				break;
			}
		}
		if (finish) {
			cout << x;
			return;
		}
	}
	cout << "INSOMNIA";
}

int main(int argc, char* argv[])
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cout << "Case #" << i + 1 << ": ";
		test();
		cout << endl;
	}
	return 0;
}
