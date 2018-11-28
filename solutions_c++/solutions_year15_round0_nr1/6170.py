//============================================================================
// Name        : Standing.cpp
//============================================================================

#include <iostream>
#include <fstream>

using namespace std;

long testCase() {

	int n;
	cin >> n;

	long invite = 0;
	long people = 0;

	char c;
	for(int i = 0; i <= n; i++) {
		cin >> c;

		int ic = c - '0';

		if (people + invite < i) {
			invite += i - (people + invite);
		}

		people += ic;
	}

	return invite;
}

int main() {
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);

	ifstream in("in.txt");
	cin.rdbuf(in.rdbuf());

	ofstream out("out.txt");
	cout.rdbuf(out.rdbuf());

	int t;
	cin >> t;

	for (int i = 0; i < t; i++) {
		cout << "Case #" << i + 1 << ": " << testCase() << '\n';
	}

	in.close();
	out.close();

	return 0;

}
