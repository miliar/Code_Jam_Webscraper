#include <iostream>
#include <string>
using namespace std;

string flip(string pan, int i){
	string aux;
	
	for (int k = i; k >= 0; k--){
		//cout << pan[k];
		if (pan[k] == '+') aux += '-';
		else aux += '+';
	}
	//cout << endl;
	
	if (pan.length() - 1 > i){
		for (int k = i + 1; k < pan.length(); k++){
			aux += pan[k];
		}	
	}
	
	return aux;
	
}

void solve (string pan){
	string copy = "";
	for (int i = 0; i < pan.length(); i++) copy += "+";
	int ans = 0;
	for (int i = pan.length() - 1; i >= 0; i--){
		if (pan[i] != copy[i]) {
			copy = flip(copy, i);
			ans++;
		}
	}
	cout << " " << ans;
}


int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++){
		cout << "Case #" << t << ":";
		string pan;
		cin >> pan;
		solve(pan);
		cout << endl;
	}
	return 0;
}
