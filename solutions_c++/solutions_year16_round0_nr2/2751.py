#include <iostream>
#include <string>
using namespace std;

int main() {
	int T;
	string str;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> str;
		int nflips = (str[str.size()-1] == '-');
		for (int i = 1; i < str.size(); i++) nflips += (str[i] != str[i-1]) ;
		cout << "Case #" << t << ": " << nflips << "\n";
	}
}
