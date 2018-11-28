#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstring>
#include <cmath>

using namespace std;

int main() {
	
	int max_shyness, people_no, friends_required, tc, i, k;
	int * people;
	
	string s;
	
	cin >> tc;
	
	k = 1;
	
	while ( tc-- ) {
		cin >> max_shyness;
		cin >> s;
		people_no = 0;
		friends_required = 0;
		
		people = new int [max_shyness+1];
		
		for ( i = 0; i <= max_shyness; i++ ) {
			people[i] = s[i] - 48;
		}
		
		for ( i = 1; i <= max_shyness; i++ ) {
			people_no = people_no + people[i - 1];
			if ( ( people[i] != 0 ) && ( i > people_no + friends_required ) )
				friends_required = i - people_no;
		}
		cout << "Case #" << k << ": " << friends_required << endl;
		k++;
	}
	
	return 0;
}