#include <iostream>
#include <string>
using namespace std;

int main()
{
	int numCases = 0;
	cin >> numCases;

	for (int i = 1; i <= numCases; ++i) {
		string s;
		string lw;
		cin >> s;

		lw.push_back(s[0]);

		for (string::size_type j = 1; j < s.length(); ++j) {
			if (s[j] >= lw[0]) {
				string x;
				x.push_back(s[j]);
				lw = x + lw;
			}
			else {
				lw += s[j];
			}
		}

		cout << "Case #" << i << ": " << lw << endl;
	}

    return 0;
}

