#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;


void work(int cases, string data) {
	vector<int> rec(255, 0);
	for (int i = 0; i < data.size(); ++i) {
		rec[data[i]]+=1;
	}
	string ans;
	while (rec['Z']) {
		ans += "0";
		rec['Z'] -= 1;rec['E'] -= 1;rec['R'] -= 1;rec['O'] -= 1;
	}
	while (rec['W']) {
		ans += "2";
		rec['T'] -= 1;rec['W'] -= 1;rec['O'] -= 1;
	}
	while (rec['U']) {
		ans += "4";
		rec['F'] -= 1;rec['O'] -= 1;rec['U'] -= 1;rec['R'] -= 1;
	}
	while (rec['X']) {
		ans += "6";
		rec['S'] -= 1;rec['I'] -= 1;rec['X'] -= 1;
	}
	while (rec['G']) {
		ans += "8";
		rec['E'] -= 1;rec['I'] -= 1;rec['G'] -= 1;rec['H'] -= 1;rec['T'] -= 1;
	}
	while (rec['T']) {
		ans += "3";
		rec['T'] -= 1;rec['H'] -= 1;rec['R'] -= 1;rec['E'] -= 2;
	}
	while (rec['F']) {
		ans += "5";
		rec['F'] -= 1;rec['I'] -= 1;rec['V'] -= 1;rec['E'] -= 1;
	}
	while (rec['S']) {
		ans += "7";
		rec['S'] -= 1;rec['E'] -= 2;rec['V'] -= 1;rec['N'] -= 1;rec['T'] -= 1;
	}
	while (rec['O']) {
		ans += "1";
		rec['O'] -= 1;
	}
	while (rec['I']) {
		ans += "9";
		rec['I'] -= 1;
	}
	sort(ans.begin(), ans.end());
	cout << "Case #" << cases << ": " << ans << endl;
}

int main() {
	freopen("A-large.in", "r", stdin);  
    freopen("A-large.out", "w", stdout);
    int N;
    string str;
    cin >> N;
    for (int i = 1; i <= N; ++i) {
    	cin >> str;
    	work(i, str);
	}
	return 0;
}
