#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
	/*freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);*/
	int t;
	cin >> t;
	for (int j = 0; j < t; j++){
		string s;
		cin >> s;
		int flippings = 0;
		for (int i = s.length() - 1; i >= 0; i--){
			if (s[i] == '-'){
				if (s[0] == '+'){
					flippings++;
					int h = 0;
					while (s[h] == '+' && h < s.length()){
						s[h] = '-';
						h++;
					}
				}

				string temp = s.substr(0, i+1);
				reverse(temp.begin(), temp.end());
				for (int h = 0; h < temp.length(); h++){
					if (temp[h] == '-'){
						temp[h] = '+';
					}
					else {
						temp[h] = '-';
					}
				}
				s = temp + s.substr(i + 1, s.length() - i);
				flippings++;
			}
		}
		cout << "Case #" << j + 1 << ": " << flippings << endl;
	}
	return 0;
}