#include <iostream>
#include <vector>
#include <algorithm>
//~ #include <string>

using namespace std;

int solve(){
	string s;
	cin >> s;
	//Caso vacio
	if (s.size() == 0) return 0;
	
	//
	int c;
	if (s[s.size()-1] == '+') c = 0; else c = 1;
	for (int i = 1; i<s.size();i++){
		if (s[i] != s[i-1]) c++;
	}
	return c;
}	

int main(){
	
	int t;
	cin >> t;
	
	for (int i = 1; i<= t; i++){
		cout << "Case #" << i << ": " << solve() << endl;
	}
	return 0;
}
