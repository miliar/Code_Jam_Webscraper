#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

bool all_happy_face(string s){
	bool flag = true;
	for(unsigned int i = 0; i < s.length(); i++){
		if(s[i] == '-'){
			return false;
		}
	}
	return flag;
}

void flip_face(string &s, char tok){
	unsigned int i = 0;
	while((s[i] != tok) && i < s.length()){
		s[i] = tok;
		i++;
	}
}

int main(){
	int T, j= 1;
	string S;
	cin >> T;
	while(T){
		cin >> S;
		int count = 0;
		while(!all_happy_face(S)){
			char c = S[0];
			char tok = (c == '-') ? '+' : '-';
			flip_face(S, tok);
			count++;
		}
		cout << "Case #" << j << ": " << count << endl;
		T--;
		j++;
	}
	return 0;
}
