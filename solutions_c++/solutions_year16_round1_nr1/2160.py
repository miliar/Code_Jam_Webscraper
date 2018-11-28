#include <iostream> 
using namespace std;

void solve_word(string s){
	if (s.size() == 0){
		return;
	} else if (s.size() == 1){
		cout << s[0];
	} else {
		int imax = 0;
		for (int i = 0; i < s.size(); i++){
			if (s[imax] <= s[i]){
				imax = i;
			}
		}
		cout << s[imax];
		solve_word(s.substr(0,imax));
		for (int i = imax + 1; i < s.size(); i++){
			cout << s[i];
		}
	}
}

void solve_case(int T){
	string s;
	cin >> s;

	cout << "Case #" << T << ": ";
	solve_word(s);
	cout << endl;
}

int main() {
  	int t;
  	cin >> t; 
  	for (int i = 1; i <= t; i++) {
  	  solve_case(i);
  	}
  	return 0;
}