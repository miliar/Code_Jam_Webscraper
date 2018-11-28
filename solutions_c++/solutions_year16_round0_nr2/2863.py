#include <iostream>
using namespace std;

string s;

int main() {
	int tc;
	cin >> tc;
	for(int z = 1; z <= tc; z++) {
		cin >> s;
		
		int flips = 0;
		for(int i = 1; i < s.size(); i++)
			if(s[i] != s[i-1])
				flips++;	
		if(s[s.size()-1]=='-')
			flips++;
		
		cout << "Case #" << z  << ": " << flips << endl;
		
	}
}
