#include <string>
#include <iostream>
#include <ctime>

using namespace std;

void trans(string& s, int k, int index){
	for(int i = 0; i < k; ++i){
		s[index + i] = (s[index + i] == '+') ? '-' : '+';
	}
}

string process(string s, int n, int k){
	int steps = 0;
	for(int i = 0 ; i < n - k + 1 ; ++i)
		if(s[i] == '-') {trans(s, k, i); steps++;}
	if(s != string(n, '+')) return string("IMPOSSIBLE");
	return to_string(steps);
}

int checkRec(string s, int i){
	if(i == s.size()) return 1;
	return s[i] == '-' ? 0 : checkRec(s, i + 1);
}

int processRec(string s, int i, int k, int sum){
	if(i >= s.size() - k + 1) {
		return checkRec(s, i) == 1 ? sum : -1;
	}
	if(s[i] == '-'){
		trans(s, k, i);
		return processRec(s, i + 1, k, sum + 1);
	} else return processRec(s, i + 1, k, sum);
}

string superProcess(string s, int k){
	int i = processRec(s, 0, k, 0);
	return i == -1 ? string("IMPOSSIBLE") : to_string(i);
}

int main(){
	/*
	srand(time(NULL));
	const int T = 100;
	for(int i = 0 ; i < T ; ++i){
		int n = rand() % 1000 + 1;
		int k = rand() % n + 1;
		string test = genCase(n, k);
		string res = process(test, n, k);
		cout << "TEST " << test << endl << "REST " << res << endl << endl;
		if(res != string(n, '+')){
			cout << "OULALALALAAL"; return -1;
		}
	}
	*/
	int T;
	cin >> T;
	for(int i = 0 ; i < T ; ++i){
		string s; int k;
		cin >> s >> k;
		cout << "Case #" << i + 1 << ": " << superProcess(s, k) << endl;
		if(superProcess(s, k) != process(s, s.size(), k)){
			cout << "OULALALALALALALA" << endl;
			return-1;
		}
	}
	return 0;
}

