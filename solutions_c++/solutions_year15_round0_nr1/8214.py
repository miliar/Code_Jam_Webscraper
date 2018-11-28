#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int main () {
	// Optimisations IO
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
	unsigned T;
	cin >> T;
	
	string line;
	getline(cin, line); // Line break
	
	for (unsigned i=1; i<=T; ++i) {
		getline(cin, line);
		stringstream sstr(line);
		
		unsigned smax;
		sstr >> smax;
		
		char shy;
		sstr.get(shy); // Space
		
		unsigned nbPeople = 0;
		unsigned nbExtraPeople = 0;
		for (unsigned level = 0; level <= smax; ++level) {
			sstr.get(shy);
			shy -= '0'; // Character 0 different from 0
			if (nbPeople < level) {
				nbExtraPeople += (level-nbPeople);
				nbPeople += (level-nbPeople);
			}
			nbPeople += shy;
		}
		
		cout << "Case #" << i << ": " << nbExtraPeople << '\n';
	}
	
	return 0;
}