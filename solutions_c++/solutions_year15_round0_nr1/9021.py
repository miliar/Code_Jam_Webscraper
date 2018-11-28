#include <iostream>
#include <string>
using namespace std;

int main() {
	int T;
	cin >> T;
	int sMax;
	string s;
	int result;
	int num;
	int newNum;
	int j = 1;
	while(T--) {
		result = 0;
		newNum = 0;
		num = 0;
		cin >> sMax;
		cin >> s;
		for(int i = 0; i <= sMax; i++) {
			if(s[i]!= '0') {
				if(newNum < i) {
					result = result + (i - newNum);
				}
			}
			num = num + (s[i] - '0');
			newNum = num + result;
		}
		
		cout << "Case #" << j << ": " << result << endl;
		j++;
	}
}