#include <iostream>
#include <sstream>
#include <math.h>

using namespace std;

string convertInt(int n) {
	stringstream ss;
	ss << n;
	return ss.str();
}

bool ispalin(string word) {
	string reversed = string();
	for(int i = 0; i <= word.length(); i++) {
		reversed.push_back(word[word.length()-i]);
	}
	bool flag = true;
	for(int j = 1; j < reversed.length(); j++) {
		// cout << word.at(j-1) << " " << reversed.at(j) << endl;
		if(word.at(j-1) != reversed.at(j)) {
			flag = false;
			break;
		}
	}
	return flag;
}

int main() {
	int T;
	cin >> T;
	for(int t = 0; t < T; t++) {
		 long long A, B;
		 cin >> A >> B;
		 // cout << A << " " << B << endl;
		 long long out = 0;
		 long long x = ceil(sqrt(A));
		 // cout << x << endl;
		 int count = pow(x, 2);
		 while(count <= B) {
		 	string s = convertInt(count);
		 	if(ispalin(s) && ispalin(convertInt(x))) {
		 		out++;
			 	// cout << s << endl;
		 	}
		 	x++;
		 	count = pow(x, 2);
		 }

		 cout << "Case #" << (t+1) << ": " << out << endl;
	}
}