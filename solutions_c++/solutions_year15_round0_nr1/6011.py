#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int tt;

int main() {
	ifstream cin("input");
	
	cin >> tt;
	for(int cc=1; cc<=tt; cc++) {
		cout << "Case #" << cc << ": ";
		
		int max;
		cin >> max;
		
		string s;
		cin >> s;
		
		int standing = 0, invited = 0;
		for(int i=0; i<max+1; i++) {
			int c = s[i] - '0'; // char to int
			if(standing < i) {
				invited++;
				standing++;
			}
			standing += c;
		}
		
		cout << invited << endl;
		
	}
	
	cin.close();
	return 0;
}
