#include <bits/stdc++.h>

using namespace std;

int main(){
	int t;
	cin >> t;
	for (int cn = 0; cn < t; cn++){
		int digits[10] = {0};
		string s;
		cin >> s;
		for (int i = 0; i < s.size(); i++){
			switch (s[i]){
				case 'Z':
					digits[0]++;
					digits[1]--;
					break;
				case 'O':
					digits[1]++;
					break;
				case 'W':
					digits[2]++;
					digits[1]--;
					break;
				case 'H':
					digits[3]++;
					break;
				case 'U':
					digits[4]++;
					digits[1]--;
					digits[5]--;
					digits[7]++;
					digits[9]++;
					break;
				case 'F':
					digits[5]++;
					digits[7]--;
					digits[9]--;
					break;
				case 'X':
					digits[6]++;
					digits[9]--;
					break;
				case 'V':
					digits[7]++;
					break;
				case 'G':
					digits[8]++;
					digits[9]--;
					digits[3]--;
					break;
				case 'I':
					//cout << "nine\n";
					digits[9]++;
					break;
			}
		}
		printf("Case #%d: ", cn+1);
		for (int i = 0; i < 10; i++){
			for (int j = 0; j < digits[i] ; j++){
				printf("%d",i);
			}
		}
		cout << endl;
	}
	return 0;
}