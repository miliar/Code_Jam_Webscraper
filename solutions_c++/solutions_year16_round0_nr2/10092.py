#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <cstring>

using namespace std;

int func(string s);
string flip(string s, int i);
map<string, int> hm;

int main(void){
	int T, ans;
	cin >> T;
	
	for(int i = 0; i < T; i++){
		string s;
		cin >> s;
		int l = s.length();
		bool found = false;
		// find first - index from right
		for(int k = l-1; k >= 0; k--){
			if(s[k] == '-'){
				found = true;
				l = k+1;
				break;
			}
		}

		if(found){
			s = s.substr(0, l);
			ans = func(s);
		}

		else ans = 0;

		cout << "Case #" << i+1 << ": " << ans << "\n";
	}
}

int func(string s){
	int min = 100000;
	if(hm.find(s) != hm.end()){
		return hm[s];
	}

	else if(s.find("-") == string::npos){
		return 0;
	}
	else if(s.find("+") == string::npos){
		return 1;
	}
	else{
		string s1;
		int l = s.length(), t;
		for(int i = 0; i < l-1; i++){
			if((s[i] == '+' && s[i+1] == '-')||(s[i] == '-' && s[i+1] == '+')){
				/*s1 = flip(s, i+1);
				if(s1 != s)
				t = 1+func(s1);
				min = min < t? min : t;*/

				s1 = flip(s, i);
				if(s1 != s)
				t = 1+func(s1);
				min = min < t? min : t;
			}
			/*else if((s[i] == '-' && s[i+1] == '+')){
				s1 = flip(s, i);
				if(!s1.equals(s))
				t = 1+func(s1);
				min = min < t? min : t;
			}*/
		}
	}

	hm.insert(pair<string, int> (s, min));
	return min;
}

string flip(string s, int i){
	int l = s.length();
	
	for(int k = 0; k <= i; k++){
		if(s[k] == '+') s[k] = '-';
		else s[k] = '+';
	}

	return s;
}
