#define _CRT_SECURE_NO_WARNINGS
#include <iostream>

#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <windows.h>

using namespace std;

string str;

int main() {
	//freopen("output.txt", "w", stdout);
	int q;
	int j = 1;
	cin >> q;
	for (; q > 0; --q) {
		int a;
		string str;
		cin >> a >> str;
		if (str == " " || str == "\n") break;
		long long cnt = 0;
		int ans = 0;
		for (int i = 0; i < (int)str.size(); ++i) {
			if (cnt < i) {
				cnt++;
				ans++;
			}
			cnt += str[i] - '0';
		}
		cout << "Case #" << j << ": " << ans << endl;
		j++;
	}
	
}