#include <iostream>
using namespace std;

int main(){
	int t;
	cin >> t;
	for(int j = 1; j <= t; j++){
		string s;
		cin >> s;

		int flips = 0;
		char lastc = '-';
		for (int i = 0; i < s.length(); ++i){
			char c = s[i];
			if(i == 0 && c == '-'){
				flips++;
			}
			if(lastc == '+' && c == '-'){
				flips+=2;
			}
			lastc = c;
		}

		cout << "Case #" << j << ": " << flips << endl;
	}
}