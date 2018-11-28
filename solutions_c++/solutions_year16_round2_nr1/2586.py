#include <iostream>
#include <string>
#include <map>

using namespace std;

int main() {
	
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	cin >> t;
	string a[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
	map<char, int> b[10];
	int order[] = {0, 2, 4, 6, 5, 8, 7, 9, 3, 1};
	int back[10];
	for (int i = 0; i < 10; ++i) {
		back[order[i]] = i;
		for (int j = 0; j < a[i].length(); ++j) {
			b[i][a[i][j]]++;
		}
	}
	for (int test = 0; test < t; ++test) {
		string str;
		cin >> str;
		map<char, int> mp;
		for (int i = 0; i < str.length(); ++i) {
			mp[str[i]]++;
		}
		printf("Case #%d: ", test + 1);
		int vals[10];
		for (int i = 0; i <= 9; ++i) {
			i = order[i];
			int cnt = 1000 * 1000 * 1000;
			for (map<char, int>::iterator it = b[i].begin(); it != b[i].end(); ++it) {
				cnt = min(cnt, mp[it->first] / it->second);
			}
			for (int j = 0; j < a[i].length(); ++j) {
				cnt = min(cnt, mp[a[i][j]]);
			}
			for (map<char, int>::iterator it = b[i].begin(); it != b[i].end(); ++it) {
				mp[it->first] -= cnt * it->second;
			}
			vals[i] = cnt;
			i = back[i];
		}
		for (int j = 0; j < 10; ++j) {
			for (int k = 0; k < vals[j]; ++k) {
				cout << j;
			}
		}
		printf("\n");
	}
    return 0;
}