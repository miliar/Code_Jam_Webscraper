#include <iostream>
#include <string>
using namespace std;

int main() {
	int t;
	cin >> t;
	for(int i=1; i<=t; ++i) {
		cout << "Case #" << i << ": ";
		string s, q="";
		cin >> s;
		for(char &c: s) {
			if(q+c>string()+c+q) q+=c;
			else q=string()+c+q;
		}
		cout << q << endl;
	}
	return 0;
}
