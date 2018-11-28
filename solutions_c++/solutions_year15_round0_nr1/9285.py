#include <iostream>
#include <vector>
#include <string>
#include <array>
#include <fstream>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int u = 0; u < t;u++) {
		int smax;
		cin >> smax;
		string s;
		cin >> s;
		int total = 0;
		int inviterte = 0;
		for (int i = 0; i < smax; i++) {
			int a = s[i] - '0';
			total += a;
			if (total < (i+1)) {
				inviterte += (i+1) - total;
				total += (i+1) - total;
			}
		}
		ofstream myfile (  "B:\\Output\\StandingOut.txt", ios::out );
		myfile << "Case #" << (u+1) << ": " << inviterte << "\n";
		myfile.close();
	}
	return 0;
}