#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <climits>
#include <cstring>

using namespace std;

bool digits[10];

bool isAsleep(int n){
	string strDigit = to_string(n);
	for (int i = 0; i < strDigit.length(); i++){
		int digit = strDigit[i] - '0';
		digits[digit] = true;
	}

	for (int i = 0; i < 10; i++){
		if (!digits[i])
			return false;
	}
	return true;
}

void main(){
	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "w", stdout);
	int testCase;
	cin >> testCase;
	for (int t = 1; t <= testCase; t++){
		memset(digits, 0, sizeof(digits));
		int n;
		cin >> n;
		if (n == 0)
			cout << "Case #" << t << ": INSOMNIA" << endl;
		else{
			int i = 1;
			while (true){
				if (isAsleep(n * i)){
					cout << "Case #" << t << ": " << n*i << endl;
					break;
				}
				else{
					i++;
				}
			}
		}
	}
}