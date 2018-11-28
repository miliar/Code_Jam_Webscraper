#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <map>
using namespace std;

void A(){
	string S;
	getline(cin, S);
	vector<string> num = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
	multiset<char> setS(S.begin(), S.end());
	vector<int> res;
	while (setS.count('Z')){
		for (char& c : num[0])setS.erase(setS.find(c));
		res.push_back(0);
	}
	while (setS.count('W')){
		for (char& c : num[2])setS.erase(setS.find(c));
		res.push_back(2);
	}
	while (setS.count('U')){
		for (char& c : num[4])setS.erase(setS.find(c));
		res.push_back(4);
	}
	while (setS.count('X')){
		for (char& c : num[6])setS.erase(setS.find(c));
		res.push_back(6);
	}
	while (setS.count('S')){
		for (char& c : num[7])setS.erase(setS.find(c));
		res.push_back(7);
	}
	while (setS.count('V')){
		for (char& c : num[5])setS.erase(setS.find(c));
		res.push_back(5);
	}
	while (setS.count('G')){
		for (char& c : num[8])setS.erase(setS.find(c));
		res.push_back(8);
	}
	while (setS.count('H')){
		for (char& c : num[3])setS.erase(setS.find(c));
		res.push_back(3);
	}
	while (setS.count('O')){
		for (char& c : num[1])setS.erase(setS.find(c));
		res.push_back(1);
	}
	while (setS.count('N')){
		for (char& c : num[9])setS.erase(setS.find(c));
		res.push_back(9);
	}
	sort(res.begin(), res.end());
	for (int& i : res) cout << i;
}
void B(){
	string str, C, J;
	getline(cin, str);
	int N = str.length() / 2;
	C = str.substr(0, N);
	J = str.substr(N + 1, N);
	string s = C, j = J;
	bool Cless = true;
	for (int i = 0; i < N; i++){
		if (C[i] == J[i]);
	}
}
void C(){
	int N;
	cin >> N; cin.ignore(INT_MAX, '\n');
	set<string> top1,top2;
	set<string> real;
	int count = 0;
	for (int i = 0; i < N; i++){
		string str;
		getline(cin, str);
		int split = str.find(' ');
		string t1 = str.substr(0, split);
		string t2 = str.substr(split + 1, str.length() - split - 1);
		if (top1.count(t1) && top2.count(t2) && !real.count(str)) count++;
		top1.insert(t1); top2.insert(t2); real.insert(str);
	}
	cout << count;
}
void D(){
	int K, C, S;
	cin >> K >> C >> S;
	if (C*S < K){
		cout << "IMPOSSIBLE";
		return;
	}
	long long tmp = 0;
	for (int k = 0; k < K; k++){
		tmp = tmp*K + k;
		if (k + 1 == K || k%C == C - 1){
			cout << tmp + 1 << " ";
			tmp = 0;
		}
	}
}

int main(){
	int T;
	cin >> T; cin.ignore(INT_MAX, '\n');
	for (int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";
		A();
		cout << endl;
	}
	return 0;
}
