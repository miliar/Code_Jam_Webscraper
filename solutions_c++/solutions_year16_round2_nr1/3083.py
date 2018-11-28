#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <cmath>
#include <map>
#include <iomanip>
#include <cctype>
#include <cstdlib>
#include <list>

using namespace std;
typedef long long lint;

string strs[] = {"ZERO", "ONE", "TWO",   "THREE", "FOUR",
                 "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int poss[] = {0, 2, 4, 5,6,7,3,1,8,9};

int count(string &s, char c) {
	int v = 0;
	for (auto &a : s)
		if (a == c)
			v++;
	return v;
}

int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		string s;
		cin >> s;
		int charc[256];
		for (int i = 0; i < 256; i++)
			charc[i] = 0;
		for (int i = 0; i < s.length(); i++) {
			charc[s[i]]++;
		}
		int cc[10];
		for (int i = 0; i < 10; i++) {
			int j = poss[i];
			cc[j] = charc[strs[j][0]] / count(strs[j], strs[j][0]);
			for (int k = 0; k < strs[j].length(); k++)
				cc[j] = min(cc[j], charc[strs[j][k]] / count(strs[j], strs[j][k]));
			cc[j] = max(cc[j], 0);
			for (int k = 0; k < strs[j].length(); k++){
				charc[strs[j][k]] -= cc[j];
			}
		}
		cout << "Case #" << (i + 1) << ": ";
		bool valid = true;
		for (int i = 0; i < s.length(); i++)
			if (charc[s[i]] > 0)
				valid = false;
		if (valid) {
			for (int i = 0; i < 10; i++)
				while (cc[i] > 0) {
					cout << i;
					cc[i]--;
				}
			cout << endl;
		}
		else cout<<"IMPOSSIBLE"<<endl;;
	}
	return 0;
}
