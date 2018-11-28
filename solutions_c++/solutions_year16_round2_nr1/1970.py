#include <iostream>
#include <map>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

#define endl '\n'
#define ll long long int

map<char, int> m;

string num[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int T;
	int Case = 1;
	cin >> T;
	while (T--){
		m.clear();
		string s;
		cin >> s;
		for (int i = 0; i < s.size(); i++){
			char a = s[i];
			m[a]++;
		}
		vector<int> ret;
		ret.clear();
		while (m['Z']){
			ret.push_back(0);
			for (int i = 0; i < num[0].size(); i++){
				m[num[0][i]]--;
			}
		}
		while (m['X']){
			ret.push_back(6);
			for (int i = 0; i < num[6].size(); i++){
				m[num[6][i]]--;
			}
		}
		while (m['S']){
			ret.push_back(7);
			for (int i = 0; i < num[7].size(); i++){
				m[num[7][i]]--;
			}
		}
		while (m['W']){
			ret.push_back(2);
			for (int i = 0; i < num[2].size(); i++){
				m[num[2][i]]--;
			}
		}
		while (m['V']){
			ret.push_back(5);
			for (int i = 0; i < num[5].size(); i++){
				m[num[5][i]]--;
			}
		}
		while (m['G']){
			ret.push_back(8);
			for (int i = 0; i < num[8].size(); i++){
				m[num[8][i]]--;
			}
		}
		while (m['H']){
			ret.push_back(3);
			for (int i = 0; i < num[3].size(); i++){
				m[num[3][i]]--;
			}
		}
		while (m['R']){
			ret.push_back(4);
			for (int i = 0; i < num[4].size(); i++){
				m[num[4][i]]--;
			}
		}
		while (m['I']){
			ret.push_back(9);
			for (int i = 0; i < num[9].size(); i++){
				m[num[9][i]]--;
			}
		}
		while (m['O']){
			ret.push_back(1);
			for (int i = 0; i < num[1].size(); i++){
				m[num[1][i]]--;
			}
		}
		sort(ret.begin(), ret.end());
		cout << "Case #" << Case << ": ";
		for (int i = 0; i < ret.size(); i++){
			cout << ret[i];
		}
		cout << endl;
		Case++;
	}
}