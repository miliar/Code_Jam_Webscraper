#include <stdio.h>
#include <string>
#include <iostream>
 
using namespace std;
 
int main(void) {
	/* number of test cases */
	unsigned short int testcases;
 
	cin >> testcases;
	string name;
	unsigned int n;
	for(unsigned int t = 1; t <= testcases; t++) {
		cin >> name;
		cin >> n;
		bool vow[name.size()];
		for(unsigned int i = 0; i < name.size(); i++) {
			if(name[i] == 'a' || name[i] == 'e' || name[i] == 'i' ||
				name[i] == 'o' || name[i] == 'u')
				vow[i] = false;
			else
				vow[i] = true;
		}

		unsigned int substrings = 0;
		unsigned int length = 0;
		for(unsigned int start = 0; start <= (name.size() - n); start++) {
			length = 0;
			for(unsigned int end = start; end < name.size(); end++) {
				if(vow[end])
					length++;
				else
					length = 0;

				if(length >= n) {
					substrings += name.size() - end;
					break;
				}
			}	

		}
		cout << "Case #" << t << ": " << substrings << endl;
	}
}
