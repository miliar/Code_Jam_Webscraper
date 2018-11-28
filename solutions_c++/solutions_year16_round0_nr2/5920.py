#include <iostream>

using namespace std;

int main() {
	int t;
	cin >> t;

	for(int cases = 1; cases <= t; cases++) {

		cin >> ws;
		string rdline;
		getline(cin, rdline);

		int reading_index = 0;
		char c = rdline[reading_index];
		char current_block = rdline[reading_index];
		int switches = 0;
		while( reading_index < (int) rdline.size() ) {

			if(c != current_block) {
				switches++;
				current_block = c;
			}

			reading_index++;
			c = rdline[reading_index];
		}
		if(current_block == '-')
			switches++;

		cout << "Case #" << cases << ": " << switches << endl;
	}
}