#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cstring>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cstdlib>

using namespace std;

int add[] = {0, 2, 6, 8, 7, 3, 5, 4, 1, 9};
string vrsta[] = {"ZERO", "TWO", "SIX", "EIGHT", "SEVEN", "THREE", "FIVE", "FOUR", "ONE", "NINE"};
char crka[] = {'Z', 'W', 'X', 'G', 'S', 'H', 'V', 'F', 'O', 'N'};

void solve(){
	vector<int> v;
	multiset<char> s;
	string str;
	cin >> str;
	int len = str.length();
	for(int i = 0; i < len; i++) s.insert(str[i]);

	for(int i = 0; i < 10; i++){
		char c = crka[i];
		while(s.find(c) != s.end()){
			int l = vrsta[i].length();
			for(int j = 0; j < l; j++) s.erase(s.find(vrsta[i][j]));
			v.push_back(add[i]);
		}
	}

	sort(v.begin(), v.end());
	for(int i = 0; i < v.size(); i++) cout << v[i];
}

int main(){
	int t;
	cin >> t;
	for(int k = 1; k <= t; k++){
		cout << "Case #" << k << ": ";
		solve();
		cout << "\n";
	}
	return 0;
}