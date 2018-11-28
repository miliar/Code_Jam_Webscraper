#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cassert>

using namespace std;
#define int long long
string mas[10]{"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
signed main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; ++tt) {
		string s;
		cin >> s;
		map <char, int> mmm;
		vector <int> ans;
		for (auto it : s) {
			mmm[it]++;
		}
		while (mmm['Z']) {
			for (auto it : mas[0]) {
				mmm[it]--;
			}
			ans.push_back(0);
		}
		while (mmm['W']) {
			for (auto it : mas[2]) {
				mmm[it]--;
				
			}
			ans.push_back(2);
		}
		while (mmm['X']) {
			for (auto it : mas[6]) {
				mmm[it]--;
				
			}
			ans.push_back(6);
		}
		while (mmm['S']) {
			for (auto it : mas[7]) {
				mmm[it]--;
				
			}
			ans.push_back(7);
		}
		while (mmm['V']) {
			for (auto it : mas[5]) {
				mmm[it]--;
				
			}
			ans.push_back(5);
		}
		while (mmm['F']) {
			for (auto it : mas[4]) {
				mmm[it]--;
				
			}
			ans.push_back(4);
		}
		while (mmm['G']) {
			for (auto it : mas[8]) {
				mmm[it]--;
				
			}
			ans.push_back(8);
		}
		while (mmm['I']) {
			for (auto it : mas[9]) {
				mmm[it]--;
				
			}
			ans.push_back(9);
		}
		while (mmm['T']) {
			for (auto it : mas[3]) {
				mmm[it]--;
				
			}
			ans.push_back(3);
		}
		while (mmm['O']) {
			for (auto it : mas[1]) {
				mmm[it]--;
				
			}
			ans.push_back(1);
		}
		sort(ans.begin(), ans.end());
		for (auto it : mmm) {
			assert(it.second == 0);
		}
		printf("Case #%d: ", tt);
		for (auto it : ans) {
			printf("%d", it);
		}
		printf("\n");
	}
}