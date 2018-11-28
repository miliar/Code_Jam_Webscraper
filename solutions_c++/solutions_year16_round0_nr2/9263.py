#include <iostream>
#include <string>

using namespace std;

string flip(string s){
	string ret = "";
	for (int i = s.length() -1 ; i >= 0 ; i--){
		if (s[i] == '+'){
			ret += '-';
		} else if (s[i] == '-'){
			ret += '+';
		}
	}
	return ret;
}

long long revenge(string s){
	if (s.length() == 1){
		if (s[0] == '+') return 0;
		if (s[0] == '-') return 1;
	}


	long long ans = 0;
	int idx = 0;
	if (s[0] == '+'){
		for (int i = 1 ; i < s.length() ; i++){
			if (s[i] == '-'){
				idx = i;
				break;
			}
		}
		if (idx == 0) return 0; // all +
		return 1 + revenge(flip(s.substr(0, idx)) + s.substr(idx, s.length() - idx));
	}
	if (s[0] == '-'){
		// search for the last -
		for (int i = s.length() -1  ; i > 0 ; i--){
			if (s[i] == '-'){
				idx = i;
				break;
			}
		}
		if (idx == 0) return 1; // just the first one is - , flip it

		return 1 + revenge(flip(s.substr(0, idx+1)));
	} 

	return -1e9;
}

int main(){
	int T;
	cin >> T;
	string s;
	for (int t = 1 ; t <= T ; t++){		
		cin >> s;
		cout << "Case #" << t << ": " << revenge(s) << endl;
	}

	return 0;
}
