#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif
#include <memory.h>
#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

bool fr[10];

int main() {

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int n, t;
	string s;
	cin >> t;

	t++;
	int l = 1;
	while (--t){
		cin >> s;

		int i;
		for (i = s.size() - 1; i >= 0; i--){
			if (s[i] == '-')break;
		}

		int c = 0;
		if (i != -1) c = 1;

		bool f1 = 1, f2 = 0;
		for (int j = i; j >= 0; j--){
			if (s[j] == '+' && f1){
				f1 = 0;
				f2 = 1;
				c++;
			}
			else if (s[j] == '-' && f2){
				f1 = 1;
				f2 = 0;
				c++;
			}
		}
		cout << "Case #" << l << ": " << c << endl;
		l++;
	}


	return 0;
}