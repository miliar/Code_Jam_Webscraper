#include <iostream>
#include <string>
#include <sstream>

using namespace std; 

int main() {
	int cases;
	string s;

	cin >> cases;

	getline(cin, s);

	for (int i = 0; i < cases; i++) {

		getline(cin, s);

		stringstream ss(s);

		int max;
		string levels;

		ss >> max >> levels;

		int people = 0;
		int peopletoadd = 0;



		for (int i = 0; i <= max; i++) {

			if (people < i) {
				peopletoadd += i - people;
				people += i - people;
				
				//cout << "peopletoadd: " << peopletoadd << endl;
			}
			people += (int)levels[i] -48;
			//cout << "people: " << people << endl;
		}

		cout << "Case #" << i + 1 << ": " << peopletoadd << endl;

	}

}