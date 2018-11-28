
#include <iostream>
#include <vector>
using namespace std;


int main() {
	// read input
        long long int ntest;
	cin >> ntest;
	for (long long int t=0; t < ntest; t++)
	{
		long long int frnd = 0;
		// read each test input
		int s_max;
		string s;
		int si;
		long long int total = 0;
		vector <int> shy;

		cin >> s_max;
		cin >> s;
		for (int i=0; i<=s_max; i++) {
			si = (int)(s.at(i) - '0');
			shy.push_back(si);
		}

		// process each test input
		total += shy.at(0);
		for (int i=1; i<=s_max; i++) {
			if (total < i) {
				frnd += (i-total);
				total += (i-total);
			}
			total += shy.at(i);
		}

		// print output
		cout << "Case #" << t+1 << ": " << frnd << endl;
	}
        return 0;
}

