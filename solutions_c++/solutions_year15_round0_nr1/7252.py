#include <iostream>
using namespace std;
int main() {
	
	int T;
	cin >> T;
	int i = 1;
	string str;
	while (i <= T) {
		int a;
		cin >> a;
		cin >> str;
		int AA = 0;
		int fn = 0;
		AA += str[0] - '0';
		for (int i = 1; i < str.length(); i++) {
			if(str[i] != '0') {
				if(AA < i) {
					fn += i - AA;
					AA += i - AA;
				}
			}
			AA += str[i] - '0';
		}
		cout << "Case #" << i << ": " <<  fn << endl;
		i++;
	}
}