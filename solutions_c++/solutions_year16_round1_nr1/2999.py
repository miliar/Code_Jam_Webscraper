#include <stdlib.h>
#include <iostream>
#include <string>

#define f(x, y) for(int x = 0; x < y; ++x)

using namespace std;

void solve(string s);

int main(){

	int T;
	string S;

	cin >> T;

	f(x, T){
		cin >> S;
		cout << "case #" << (x + 1) << ": ";
		solve(S);
	}


	return 0;
}

void solve(string s){

	string final_word = "";
	f(x, s.size()){
		if(final_word[0] <= s[x]){
			final_word.insert(final_word.begin(), s[x]);
		}else{
			final_word.push_back(s[x]);
		}
	}
	cout << final_word << endl;
}
