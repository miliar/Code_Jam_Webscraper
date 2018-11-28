#include <iostream>
#include <string>

using namespace std;

int main(void) {
	int t;
	cin >> t;
	for(int j = 1; j <= t; j++) {
		int n;
		cin >> n;
		string str;
		cin >> str;
		int cnt = 0;
		int inv = 0;
		for(int i = 0; i < n; i++) {
			cnt += str[i]-'0';
			if(cnt < i+1) {
				inv = inv+(i+1-cnt);
				cnt = i+1;
			}
		}
		//if(str[0] == '0') inv++;
		cout << "Case #" << j << ": " << inv << endl;
	}
	return 0;
} 
