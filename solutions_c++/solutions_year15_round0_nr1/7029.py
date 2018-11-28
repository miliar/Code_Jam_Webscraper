#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <string>
#include <algorithm>
#include <stdio.h>
using namespace std;
int main(){
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	unsigned int t;
	cin >> t;
	for (unsigned int i = 0; i < t; i++){
		unsigned int s;
		string str;
		cin >> s >> str;
		unsigned int res = 0;
		for (unsigned int j = 0; j < str.size(); j++){
			unsigned int count = 0;
			if (str[j] == '0') continue;
			for (int h = j - 1; h >= 0 ; h--) count += (str[h] - '0');
			count += res;
			if (count < j) res += (j - count);
		}
		cout << "Case #" << i + 1 << ": " << res << endl;
	}
	return 0;
}