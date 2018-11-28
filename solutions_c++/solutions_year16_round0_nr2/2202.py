#include <iostream>

using namespace std;

bool all_happy(string s){
	for (char i: s){
		if(i == '-') return false;
	}
	return true;
}

int last_sad(string s){
	for(int i = s.length(); i >= 0; i--){
		if(s[i] == '-') return i;
	}
	return 0;
}

int first_sad(string s){
	for(int i = 0; i < s.length(); i++){
		if(s[i] == '-') return i;
	}
	return s.length();
}



string flip (string s,int pos){
	string tmp = "";
	int i = pos;
	while(i >= 0){
		tmp += (s[i] == '+')?'-':'+';
		i--;
	}
	i=pos+1;
	while(i < s.length()){
		tmp+=s[i++];
	}
	return tmp;
}

int main(){
	int t,i,j=1;
	string s;
	// cin >> s;
	// cout << flip(s,last_sad(s));
	cin >> t;
	while(t--){
		cin >> s;
		i = 0;
		while(!all_happy(s)){
			// cout << s;
			if(s[0] == '-'){
				s = flip(s,last_sad(s));
			} else {
				s = flip(s,first_sad(s)-1);
			}
			i++;
		}
		cout << "Case #" << j++ << ": " << i << endl;
	}
	return 0;
}