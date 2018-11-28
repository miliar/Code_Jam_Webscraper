#include <iostream>
#include <fstream>

using namespace std;

int main() {
	ifstream cin ("input.txt");
	ofstream cout ("output.txt");
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cout << "Case #" << i + 1 << ": ";
		long long n;
		cin >> n;
		if (n == 0) {
			cout << "INSOMNIA" << endl;
			continue;
		}
		long long count = 0;
		long long curn = 0;
		while (count != (1<<10)-1) {
			curn += n;
			long long tempn = curn;
			while (tempn) {
				count |= (1<<(tempn%10));
				tempn /= 10;
			}
		}
		cout << curn << endl;
	}
}