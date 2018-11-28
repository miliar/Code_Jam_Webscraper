#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main() {

	int T = 0, N = 0,res = 0;
	cin >> T;
	string line;
	int length = 0;

	getline(cin, line);
	for (int i = 0; i < T; i++) {
		res = 0;
		getline(cin, line);
		length = line.length();
		char c='0', p='0', g;
		for (int k = 0; k < length; k++) {
			c = line[k];
			if(k){
				if (c != p)
					res++;
			}

			p = c;
		}
		if (p == '-')
			res++;
		cout << "Case #" << i + 1 << ": ";
		
		cout << res<<endl;
	}
	return 0;
}