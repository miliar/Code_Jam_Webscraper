#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;
int count(string s1, string s2){
	int n = 0;
	if(s1[0] != s2[0]) return -1;
	for(int i = 1; i < min(s1.length(), s2.length()); ++i){
		if(s1 == s2){
			return n;
		}
		if(s1[i] == s2[i]){
			continue;
		}
		if(s1[i-1] == s1[i]){
			s1.erase(i,1);
			--i;
			++n;
		} else if(s2[i-1] == s2[i]){
			s2.erase(i,1);
			--i;
			++n;
		} else{
			return -1;
		}
	}
	while(s1.length () != s2.length()){
		string &s = (s1.length() > s2.length() ? s1:s2);
		int i = min(s1.length(), s2.length());
		if(s[i-1] == s[i]) {
			s.erase(i, 1);
			++n;
		}else return -1;
	}
	if(s1 == s2) return n;
	return -1;
}

void output(int i, string s){
	cout << "Case #" << i << ": " << s << endl;
}
int main(){
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i){
		int n;
		cin >> n;
		vector<string> v;
		for(int j = 0; j < n; ++j){
			string s;
			cin >> s;
			v.push_back(s);
		}
		bool impossible = false;
		int cmax = 0;
		for(int j = 0; j < n; ++j){
			for(int k = 0; k < n; ++k){
				int c = count(v[j], v[k]);
				if(c < 0){
					impossible = true;
				}
				cmax = max(cmax, c);
			}
		}
		if(impossible){
			output(i, "Fegla Won");
		}else{
			stringstream s;
			s << cmax;
			output(i, s.str());
		}
	}
}

