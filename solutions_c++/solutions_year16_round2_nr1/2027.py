#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <iomanip>
#include <conio.h>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main(){
	//freopen("input.txt", "r", stdin); 
	//freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	int alph[26] = { 0 };

	for (int i = 0; i < t; i++){
		string s;
		cin >> s;
		for (int j = 0; j < s.length(); j++){
			alph[s[j] - 'A']++;
		}
		vector<int> ans;
		while (alph['Z' - 'A']){
			ans.push_back(0);
			alph['Z' - 'A']--;
			alph['E' - 'A']--;
			alph['R' - 'A']--;
			alph['O' - 'A']--;
		}
		while (alph['W' - 'A']){
			ans.push_back(2);
			alph['T' - 'A']--;
			alph['W' - 'A']--;
			alph['O' - 'A']--;
		}
		while (alph['U' - 'A']){
			ans.push_back(4);
			alph['F' - 'A']--;
			alph['O' - 'A']--;
			alph['U' - 'A']--;
			alph['R' - 'A']--;
		}
		while (alph['X' - 'A']){
			ans.push_back(6);
			alph['S' - 'A']--;
			alph['I' - 'A']--;
			alph['X' - 'A']--;
		}
		while (alph['G' - 'A']){
			ans.push_back(8);
			alph['E' - 'A']--;
			alph['I' - 'A']--;
			alph['G' - 'A']--;
			alph['H' - 'A']--;
			alph['T' - 'A']--;
		}
		while (alph['O' - 'A']){
			ans.push_back(1);
			alph['O' - 'A']--;
			alph['N' - 'A']--;
			alph['E' - 'A']--;
		}
		while (alph['H' - 'A']){
			ans.push_back(3);
			alph['T' - 'A']--;
			alph['H' - 'A']--;
			alph['R' - 'A']--;
			alph['E' - 'A']--;
			alph['E' - 'A']--;
		}
		while (alph['F' - 'A']){
			ans.push_back(5);
			alph['F' - 'A']--;
			alph['I' - 'A']--;
			alph['V' - 'A']--;
			alph['E' - 'A']--;
			
		}
		while (alph['S' - 'A']){
			ans.push_back(7);
			alph['S' - 'A']--;
			alph['E' - 'A']--;
			alph['V' - 'A']--;
			alph['E' - 'A']--;
			alph['N' - 'A']--;
		}
		while (alph['I' - 'A']){
			ans.push_back(9);
			alph['N' - 'A']--;
			alph['I' - 'A']--;
			alph['N' - 'A']--;
			alph['E' - 'A']--;
		}
		sort(ans.begin(), ans.end());
		cout << "Case #" << i + 1 << ": ";
		for (int j = 0; j < ans.size(); j++){
			cout << ans[j];
		}
		cout << endl;
	}
	return 0;
}
