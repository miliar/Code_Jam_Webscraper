#include <bits/stdc++.h>
using namespace std;

typedef vector<int> VI;
int main(){
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i){
		string s;
		cin >> s;
		int counter = 0;
		char aux = '=';
		int sz = s.size();
		for (int j = 0; j < sz; ++j){
			if (s[j] != aux) ++counter;
			aux = s[j]; 
		}
		if (s[sz-1] == '+' ) --counter;
		cout << "Case #" << i+1 <<": " << counter << '\n'; 
		
	}
	
	
}
