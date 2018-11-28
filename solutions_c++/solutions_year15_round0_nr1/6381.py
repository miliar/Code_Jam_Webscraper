#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include<string>
#include<stdlib.h>
using namespace std;

int main() {

	freopen("C:/Users/HP/Desktop/src.txt", "r", stdin);
	freopen("C:/Users/HP/Desktop/out.txt", "w", stdout);
	string s;
	int t, m;

	cin >> t;

	for (int j = 0; j<t; j++){
		cin >> m;

		cin >> s;
		int c = 0, res = 0;
		for (int i = 0; i<m + 1; i++){
			c += s[i] - '0';
			//	cout<<c;
			if (i + 1>c && s[i + 1] != '0'){
				res += (i + 1 - c);
				c += i + 1 - c;
			}

		}

		cout << "Case #" << j + 1 << ": " << res << endl;
	}

	return 0;
}